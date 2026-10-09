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
