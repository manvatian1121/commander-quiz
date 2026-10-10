// UI 冒烟测试：用最小 DOM 桩把完整答题流程（含分支跳转）跑一遍，确认界面层不会报错。
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const html = fs.readFileSync(path.join(ROOT, "commander_quiz.html"), "utf8");

/* ---------- 取数据 ---------- */
const payloadMatch = html.match(
  /<script id="payload" type="application\/json">([\s\S]*?)<\/script>/);
if (!payloadMatch) throw new Error("找不到 payload");
const payloadText = payloadMatch[1].replace(/<\\\//g, "</");
globalThis.__QUIZ_DATA__ = JSON.parse(payloadText);

/* ---------- 最小 DOM 桩 ---------- */
class Node {
  constructor(tag) {
    this.tag = tag; this.className = ""; this._html = ""; this.textContent = "";
    this.children = []; this.onclick = null; this.disabled = false;
    this.style = { setProperty() {} };
  }
  // 与真实 DOM 一致：设置 innerHTML 会清空原有子节点
  set innerHTML(v) { this._html = String(v); this.children = []; }
  get innerHTML() { return this._html + this.children.map((c) => c.innerHTML).join(""); }
  appendChild(child) { this.children.push(child); return child; }
  removeChild(child) { return child; }
  setAttribute() {}
  select() {}
  // 桩不做真实的选择器匹配：返回空集合，让调用方的 forEach 安全跳过。
  // 主将池的过滤/排序逻辑由 poolList() 单独测。
  querySelectorAll() { return []; }
  querySelector() { return null; }
}
const byId = {};
let copiedViaExec = false;
const document = {
  body: new Node("body"),
  createElement: (tag) => new Node(tag),
  getElementById: (id) => {
    if (id === "payload") return { textContent: payloadText };
    if (!byId[id]) byId[id] = new Node("div#" + id);
    return byId[id];
  },
  execCommand: (cmd) => { if (cmd === "copy") { copiedViaExec = true; return true; } return false; },
};
globalThis.document = document;
globalThis.window = { scrollTo() {}, prompt: () => {} };
try { Object.defineProperty(globalThis.navigator, "clipboard", { value: undefined, configurable: true }); }
catch (e) { /* Node 的 navigator 不可改时忽略 */ }

/* ---------- 执行应用脚本 ---------- */
const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)];
(0, eval)(scripts[scripts.length - 1][1]);
const engine = globalThis.__quizEngine;
if (!engine) throw new Error("__quizEngine 未暴露");

const problems = [];
function check(label, fn) {
  try { fn(); console.log(`  ✓ ${label}`); }
  catch (error) { problems.push(`${label}: ${error.message}`); console.log(`  ✗ ${label} — ${error.message}`); }
}
const rendered = () => (byId["app"] ? byId["app"].innerHTML : "");
const onResult = () => rendered().includes("最适合你的主将");

/** 走一遍流程；picker(q, step) 返回要选的选项下标 */
function walk(mode, picker, limit = 400) {
  engine.start(mode);
  const visited = [];
  let steps = 0;
  while (steps < limit) {
    if (onResult()) return { visited, steps, finished: true };
    const st = engine.getState();
    const q = engine.Q.byId[st.current];
    if (!q) return { visited, steps, finished: false };
    visited.push(q.id);
    const idx = picker(q, steps) % q.opts.length;
    if (q.multi) {
      const take = Math.min(q.multi, q.opts.length);
      const chosen = [];
      for (let c = 0; c < take; c++) chosen.push((idx + c) % q.opts.length);
      chosen.forEach((c) => engine.choose(q, c));
      engine.goNext(null);
    } else {
      engine.choose(q, idx);
    }
    steps++;
  }
  return { visited, steps, finished: false };
}

/* ---------- 场景 1：完整版 ---------- */
console.log("\n[场景 1] 完整版全流程");
let fullRun = null;
check("能一路走到结果页", () => {
  fullRun = walk("full", () => 0);
  if (!fullRun.finished) throw new Error(`走了 ${fullRun.steps} 题仍未出结果`);
});
check("作答题数落在预估区间内", () => {
  const b = engine.totals.fullBounds;
  if (fullRun.visited.length < b[0] || fullRun.visited.length > b[1]) {
    throw new Error(`实际 ${fullRun.visited.length} 题，预估区间 ${b[0]}~${b[1]}`);
  }
});
check("确实走了分支衍生题", () => {
  const spineSet = new Set(engine.spine);
  const branches = fullRun.visited.filter((id) => !spineSet.has(id));
  if (branches.length < 3) throw new Error(`只走到 ${branches.length} 道分支题`);
});
check("结果页渲染出主将名与介绍", () => {
  const out = rendered();
  if (!out.includes("最适合你的主将")) throw new Error("缺结果标题");
  if (!out.includes("这套牌在干什么")) throw new Error("缺介绍");
  if (!out.includes("怎么组")) throw new Error("缺建牌思路");
  if (!out.includes("常见搭配")) throw new Error("缺搭配牌");
  const named = globalThis.__QUIZ_DATA__.commanders.filter((c) => out.includes(c.zh || c.en));
  if (!named.length) throw new Error("结果页没有任何主将名");
});

/* ---------- 场景 2：不同选项组合都能走通 ---------- */
console.log("\n[场景 2] 各种选项组合都要能走通");
["全选B", "全选C", "全选D", "交替", "末尾选项"].forEach((label, i) => {
  check(`策略「${label}」能走到结果页`, () => {
    const pickers = [() => 1, () => 2, () => 3, (q, s) => s % 3, (q) => q.opts.length - 1];
    const run = walk("full", pickers[i]);
    if (!run.finished) throw new Error(`走了 ${run.steps} 题仍未出结果`);
  });
});

/* ---------- 场景 2b：玩法画像不能出现负数 ---------- */
// 偏好向量做过中心化处理，本身可以是负值；但画成「越渴望越长」的条形图时，
// 负值会显示成 -4% 这种误导性数字（用户会以为系统推荐错了）。
// 这里对多种答题策略逐一检查结果页里有没有负数百分比。
console.log("\n[场景 2b] 玩法画像不出现负数百分比");
const STRATEGIES = {
  全选A: () => 0, 全选B: () => 1, 全选C: () => 2, 全选D: () => 3, 全选E: () => 4,
  交替: (q, s) => s % 3, 末尾: (q) => q.opts.length - 1,
};
Object.entries(STRATEGIES).forEach(([label, picker]) => {
  check(`「${label}」的画像没有负数`, () => {
    const run = walk("full", picker);
    if (!run.finished) throw new Error("没走到结果页");
    const out = rendered();
    const section = out.slice(out.indexOf("你的玩法画像"), out.indexOf("你的经验段"));
    if (!section) throw new Error("结果页没有玩法画像");
    const bad = section.match(/-\s*\d+(\.\d+)?%/g);
    if (bad) throw new Error(`出现负数百分比：${bad.join("、")}`);
    // 条形宽度也不能是负数（非法 CSS）
    const widths = [...section.matchAll(/width:\s*(-?[\d.]+)%/g)].map((m) => parseFloat(m[1]));
    if (widths.some((w) => w < 0)) throw new Error(`条形宽度为负：${widths.join("、")}`);
    if (widths.some((w) => w > 100)) throw new Error(`条形宽度超过 100%：${widths.join("、")}`);
  });
});

/* ---------- 场景 3：快速版 ---------- */
console.log("\n[场景 3] 快速版");
check("快速版能走到结果页且题数少于完整版", () => {
  const run = walk("quick", () => 0);
  if (!run.finished) throw new Error("快速版没走到结果页");
  if (run.visited.length >= engine.totals.fullBounds[0]) {
    throw new Error(`快速版 ${run.visited.length} 题，不比完整版 ${engine.totals.fullBounds[0]} 少`);
  }
  const qb = engine.totals.quickBounds;
  if (run.visited.length < qb[0] || run.visited.length > qb[1]) {
    throw new Error(`实际 ${run.visited.length} 题，预估区间 ${qb[0]}~${qb[1]}`);
  }
});

/* ---------- 场景 4：回上一题 ---------- */
console.log("\n[场景 4] 回上一题");
check("回退后能重新答，且改答案生效", () => {
  engine.start("full");
  const first = engine.getState().current;
  const q0 = engine.Q.byId[first];
  engine.choose(q0, 0);
  engine.goBack();
  if (engine.getState().current !== first) throw new Error("回退没有回到上一题");
  engine.choose(q0, 1);
  if (engine.getState().answers[first] !== 1) throw new Error("改答案没生效");
});

/* ---------- 场景 5：多选题 ---------- */
console.log("\n[场景 5] 多选题");
check("多选题能选多个且受上限约束", () => {
  engine.start("full");
  const multiIds = engine.Q.all.filter((q) => q.multi).map((q) => q.id);
  if (!multiIds.length) throw new Error("题库里没有多选题");
  const q = engine.Q.byId[multiIds[0]];
  engine.choose(q, 0);
  engine.choose(q, 1);
  const picked = engine.getState().answers[q.id];
  if (!Array.isArray(picked) || picked.length !== 2) throw new Error("多选没有记录两项");
  for (let i = 2; i < q.opts.length; i++) engine.choose(q, i);
  if (engine.getState().answers[q.id].length > q.multi) throw new Error("突破了 multi 上限");
});

/* ---------- 场景 6：复制按钮 ---------- */
console.log("\n[场景 6] 复制结果按钮");
check("点击后不抛异常且复制成功", () => {
  walk("quick", () => 0);
  const btn = byId["copy"];
  if (!btn || typeof btn.onclick !== "function") throw new Error("找不到复制按钮");
  btn.onclick.call(btn);
  if (!copiedViaExec && btn.textContent !== "已复制 ✓") throw new Error("复制未生效");
});

/* ---------- 场景 8：主将池浏览 ---------- */
console.log("\n[场景 8] 主将池浏览");
check("能打开主将池且不抛异常", () => {
  engine.screenPool();
  const out = document.getElementById("pool-list").innerHTML;
  if (!out.includes("poolrow")) throw new Error("列表没有渲染出主将行");
});

check("主将池列出全部主将并按流行度排序", () => {
  const total = globalThis.__QUIZ_DATA__.commanders.length;
  const P = engine.POOL;
  P.kw = ""; P.color = ""; P.sort = "pop";
  const list = engine.poolList();
  if (list.length !== total) throw new Error(`列出 ${list.length} 位，应为 ${total} 位`);
  for (let i = 1; i < list.length; i++) {
    if ((list[i - 1].num_decks || 0) < (list[i].num_decks || 0)) {
      throw new Error("按流行度排序时有逆序");
    }
  }
});

check("颜色多选与「不包含未选颜色」", () => {
  const P = engine.POOL, cmds = globalThis.__QUIZ_DATA__.commanders;
  P.kw = ""; P.tags = []; P.brackets = []; P.strict = false; P.sort = "pop";

  for (const color of ["W", "U", "B", "R", "G"]) {
    P.colors = [color];
    const got = engine.poolList();
    const want = cmds.filter((c) => c.colors.indexOf(color) >= 0).length;
    if (got.length !== want) {
      throw new Error(color + " 色筛出 " + got.length + "，应为 " + want);
    }
  }
  P.colors = ["C"];
  const none = engine.poolList();
  const wantNone = cmds.filter((c) => c.colors === "C").length;
  if (none.length !== wantNone) {
    throw new Error("无色筛出 " + none.length + "，应为 " + wantNone);
  }
  if (none.some((c) => c.colors !== "C")) throw new Error("无色筛选混进了有色主将");

  P.colors = ["W", "U"];
  const or = engine.poolList();
  const wantOr = cmds.filter((c) => c.colors.indexOf("W") >= 0
                                 || c.colors.indexOf("U") >= 0).length;
  if (or.length !== wantOr) {
    throw new Error("W|U 多选筛出 " + or.length + "，应为 " + wantOr);
  }
  if (or.length <= none.length) throw new Error("多选结果没有比单选更多，OR 逻辑可疑");

  P.colors = ["W", "U"]; P.strict = true;
  const strict = engine.poolList();
  if (strict.some((c) => c.colors.split("").some((x) => ["W", "U"].indexOf(x) < 0))) {
    throw new Error("严格模式筛出了含未选颜色的主将");
  }
  if (strict.length >= or.length) throw new Error("严格模式的结果没有比 OR 模式更少");
  if (strict.some((c) => c.colors === "C")) throw new Error("严格模式下无色主将漏了进来");
  P.strict = false; P.colors = [];
});

check("主将池的筛选片都能正常渲染（不出现 undefined）", () => {
  engine.screenPool();
  // DOM 桩的 getElementById 会新建空节点，所以要从 app 读整块渲染结果
  const html = document.getElementById("app").innerHTML;
  if (html.indexOf("undefined") >= 0) {
    const i = html.indexOf("undefined");
    throw new Error("界面上出现 undefined：" + html.slice(Math.max(0, i - 60), i + 30));
  }
  if (html.indexOf("NaN") >= 0) throw new Error("界面上出现 NaN");

  // 20 个玩法标签、6 个颜色片、5 个强度档位都要在
  const tags = engine.poolTags();
  if (tags.length !== 20) throw new Error("玩法标签应有 20 个，实得 " + tags.length);
  for (const o of tags) {
    if (!o.zh) throw new Error("标签 " + o.k + " 没有中文名");
    if (html.indexOf(o.zh) < 0) throw new Error("标签「" + o.zh + "」没有渲染出来");
  }
  for (const label of ["白", "蓝", "黑", "红", "绿", "无色"]) {
    if (html.indexOf(">" + label + "<") < 0) throw new Error("颜色片「" + label + "」没渲染");
  }
  for (const b of ["B1", "B2", "B3", "B4", "B5"]) {
    if (html.indexOf(">" + b + "<") < 0) throw new Error("档位片「" + b + "」没渲染");
  }
});

check("玩法偏好筛选", () => {
  const P = engine.POOL = engine.POOL;
  P.colors = []; P.brackets = []; P.strict = false;

  P.tags = ["chaos"];
  const chaos = engine.poolList();
  if (!chaos.length) throw new Error("「随机搞事」筛出 0 位，可疑");
  if (chaos.some((c) => (c.vec.chaos || 0) < 1.0)) {
    throw new Error("混进了混沌轴不足的主将");
  }

  P.tags = ["chaos", "combo"];
  const both = engine.poolList();
  if (both.some((c) => (c.vec.chaos || 0) < 1.0 || (c.vec.combo || 0) < 1.0)) {
    throw new Error("多标签应是「全部命中」而不是「任一命中」");
  }
  if (both.length > chaos.length) throw new Error("加了标签结果反而变多");

  const all = engine.poolTags().map((o) => o.k);
  if (all.length !== 20) throw new Error("玩法标签应有 20 个，实得 " + all.length);
  for (const k of all) {
    P.tags = [k];
    const r = engine.poolList();
    if (!r.length) throw new Error("标签 " + k + " 筛出 0 位");
    if (r.some((c) => (c.vec[k] || 0) < 1.0)) {
      throw new Error("标签 " + k + " 的结果里有不达标的");
    }
  }
  P.tags = [];
});

check("强度档位筛选", () => {
  const P = engine.POOL, cmds = globalThis.__QUIZ_DATA__.commanders;
  P.colors = []; P.tags = []; P.strict = false;
  for (const b of ["1", "2", "3", "4", "5"]) {
    P.brackets = [b];
    const got = engine.poolList();
    const want = cmds.filter((c) => String(c.bracket) === b).length;
    if (got.length !== want) {
      throw new Error("B" + b + " 筛出 " + got.length + "，应为 " + want);
    }
  }
  P.brackets = ["4", "5"];
  const hi = engine.poolList();
  if (hi.some((c) => ["4", "5"].indexOf(String(c.bracket)) < 0)) {
    throw new Error("B4|B5 混进了低档位主将");
  }
  if (!hi.length) throw new Error("B4|B5 筛出 0 位");
  P.brackets = [];
});

check("筛选条件可以叠加", () => {
  const P = engine.POOL, cmds = globalThis.__QUIZ_DATA__.commanders;
  P.colors = ["B"]; P.tags = ["removal"]; P.brackets = ["2", "3"];
  const got = engine.poolList();
  const want = cmds.filter((c) => c.colors.indexOf("B") >= 0
      && (c.vec.removal || 0) >= 1.0
      && ["2", "3"].indexOf(String(c.bracket)) >= 0).length;
  if (got.length !== want) {
    throw new Error("叠加筛出 " + got.length + "，应为 " + want);
  }
  if (!got.length) throw new Error("叠加筛选结果为空，条件可能互斥得过死");
  P.colors = []; P.tags = []; P.brackets = [];
});

check("清空筛选能恢复全部", () => {
  const P = engine.POOL, total = globalThis.__QUIZ_DATA__.commanders.length;
  P.kw = ""; P.colors = []; P.tags = []; P.brackets = []; P.strict = false;
  if (engine.poolList().length !== total) throw new Error("清空后没有恢复全部主将");
});

check("搜索能按中英文名过滤", () => {
  const P = engine.POOL;
  P.kw = "玛切莎"; P.color = "";
  if (!engine.poolList().some((c) => c.en === "Queen Marchesa")) throw new Error("中文名搜不到");
  P.kw = "queen marchesa";
  const enHit = engine.poolList();
  if (enHit.length !== 1 || enHit[0].en !== "Queen Marchesa") {
    throw new Error(`英文名搜索结果异常：${enHit.length} 条`);
  }
  P.kw = "zzzz没有这个主将zzzz";
  if (engine.poolList().length !== 0) throw new Error("无匹配时应返回空列表");
  P.kw = "";
});

check("三种排序都能用", () => {
  const P = engine.POOL;
  P.kw = ""; P.color = "";
  for (const sort of ["pop", "diff", "name"]) {
    P.sort = sort;
    const list = engine.poolList();
    if (!list.length) throw new Error(`排序 ${sort} 返回空列表`);
  }
  P.sort = "diff";
  const byDiff = engine.poolList();
  for (let i = 1; i < byDiff.length; i++) {
    if ((byDiff[i - 1].difficulty || 0) > (byDiff[i].difficulty || 0)) {
      throw new Error("按难度排序时有逆序");
    }
  }
  P.sort = "pop";
});

check("排序方向可以翻转", () => {
  const P = engine.POOL, S = engine.POOL_SORTS;
  const cmds = globalThis.__QUIZ_DATA__.commanders;
  P.kw = ""; P.colors = []; P.tags = []; P.brackets = []; P.strict = false;

  // 每个字段的两个方向都必须自洽，且互为逆序
  for (const key of ["pop", "diff", "salt", "name"]) {
    const field = { pop:"num_decks", diff:"difficulty", salt:"salt", name:"zh" }[key];
    for (const desc of [false, true]) {
      P.sort = key; S[key].desc = desc;
      const list = engine.poolList();
      if (list.length !== cmds.length) {
        throw new Error(key + " 排序后条目数不对：" + list.length);
      }
      for (let i = 1; i < list.length; i++) {
        const a = list[i - 1][field], b = list[i][field];
        if (field === "zh") {
          const c = String(a).localeCompare(String(b), "zh");
          if (desc ? c < 0 : c > 0) throw new Error(key + " 名称方向错了");
        } else {
          const av = a || 0, bv = b || 0;
          if (desc ? av < bv : av > bv) {
            throw new Error(key + " desc=" + desc + " 时出现逆序");
          }
        }
      }
    }
    S[key].desc = (key === "pop" || key === "salt");
  }

  // 翻过来之后第一位应该换人（至少在最极端的两个字段上）
  P.sort = "pop"; S.pop.desc = true;
  const hottest = engine.poolList()[0].en;
  S.pop.desc = false;
  const coldest = engine.poolList()[0].en;
  if (hottest === coldest) throw new Error("流行度翻转方向后第一位没变");
  const nH = globalThis.__QUIZ_DATA__.commanders.find((c) => c.en === hottest).num_decks;
  const nC = globalThis.__QUIZ_DATA__.commanders.find((c) => c.en === coldest).num_decks;
  if (!(nH > nC)) throw new Error("降序第一位应比升序第一位更热门");
  S.pop.desc = true;
  P.sort = "pop";
});

check("每位主将都有可展开的介绍文", () => {
  const desc = globalThis.__QUIZ_DATA__.descriptions;
  const missing = globalThis.__QUIZ_DATA__.commanders.filter(
    (c) => !desc[c.en] || !desc[c.en].intro);
  if (missing.length) throw new Error(`${missing.length} 位主将缺介绍文`);
});

/* ---------- 场景 7：内容完整性 ---------- */
console.log("\n[场景 7] 内嵌数据完整性");
check("每位主将都有介绍文与搭配牌", () => {
  const d = globalThis.__QUIZ_DATA__;
  d.commanders.forEach((c) => {
    if (!d.descriptions[c.en]) throw new Error(`${c.en} 缺介绍文`);
    const picks = d.cardDisplay[c.en];
    if (!picks || !picks.synergy || !picks.synergy.length) throw new Error(`${c.en} 缺搭配牌`);
  });
});
check("每题都有中文分野名与选项文本", () => {
  engine.Q.all.forEach((q) => {
    if (!q.secName) throw new Error(`${q.id} 缺 secName`);
    q.opts.forEach((o, i) => {
      if (!o.t || !o.t.trim()) throw new Error(`${q.id} 选项${i} 为空`);
    });
  });
});

console.log("\n" + "=".repeat(64));
if (problems.length) {
  console.log(`✗ UI 冒烟测试发现 ${problems.length} 个问题：`);
  problems.forEach((p) => console.log(`  - ${p}`));
  process.exit(1);
} else {
  console.log("✓ UI 冒烟测试全部通过");
}
