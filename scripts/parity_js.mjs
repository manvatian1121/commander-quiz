// 一致性测试：从构建好的 HTML 里抽出真实内联脚本，在 Node 里走完整分支流程，
// 产出答案集与分数，供 parity_compare.py 与 Python 引擎比对。
// 产物：data/js_results.json
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

/* ---------- 最小 DOM 桩（走流程要用到渲染） ---------- */
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
const document = {
  body: new Node("body"),
  createElement: (tag) => new Node(tag),
  getElementById: (id) => {
    if (id === "payload") return { textContent: payloadText };
    if (!byId[id]) byId[id] = new Node("div#" + id);
    return byId[id];
  },
  execCommand: () => true,
};
globalThis.document = document;
globalThis.window = { scrollTo() {}, prompt: () => {} };

/* ---------- 执行应用脚本 ---------- */
const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)];
(0, eval)(scripts[scripts.length - 1][1]);
const engine = globalThis.__quizEngine;
if (!engine) throw new Error("引擎钩子未暴露（__quizEngine 缺失）");

/* ---------- 走一遍流程，记录答案 ---------- */
function walk(mode, picker) {
  engine.start(mode);
  const answers = {};
  const visited = [];
  for (let step = 0; step < 500; step++) {
    const rendered = byId["app"] ? byId["app"].innerHTML : "";
    if (rendered.includes("最适合你的主将")) {
      return { answers, visited, finished: true, steps: step };
    }
    const st = engine.getState();
    const q = engine.Q.byId[st.current];
    if (!q) return { answers, visited, finished: false, steps: step };
    visited.push(q.id);
    const idx = picker(q, step) % q.opts.length;
    if (q.multi) {
      const take = Math.min(q.multi, q.opts.length);
      const chosen = [];
      for (let c = 0; c < take; c++) chosen.push((idx + c) % q.opts.length);
      chosen.forEach((c) => engine.choose(q, c));
      answers[q.id] = chosen;
      engine.goNext(null);
    } else {
      engine.choose(q, idx);
      answers[q.id] = idx;
    }
  }
  return { answers, visited, finished: false, steps: 500 };
}

const PICKERS = {
  "全选A": () => 0,
  "全选B": () => 1,
  "全选C": () => 2,
  "全选D": () => 3,
  "交替": (q, step) => step % 3,
  "末尾选项": (q) => q.opts.length - 1,
};

const out = { sets: {}, meta: { commanders: globalThis.__QUIZ_DATA__.commanders.length } };

for (const [name, picker] of Object.entries(PICKERS)) {
  const full = walk("full", picker);
  if (!full.finished) throw new Error(`【${name}】完整版没走到结果页（走了 ${full.steps} 步）`);
  engine.setAnswers(full.answers);
  const t = engine.tally();
  const ranked = engine.rank(t);
  out.sets[name] = {
    mode: "full",
    steps: full.steps,
    answers: full.answers,
    visited: full.visited,
    constraints: {
      complex: +t.cons.complex.toFixed(4),
      budget: +t.cons.budget.toFixed(4),
      salt: +t.cons.salt.toFixed(4),
      exp: t.cons.exp,
    },
    top: ranked.slice(0, 12).map((r) => ({ en: r.c.en, score: +r.score.toFixed(4) })),
    scores: Object.fromEntries(ranked.map((r) => [r.c.en, +r.score.toFixed(6)])),
  };
}

// 快速版单独走一遍，确认题序跳转正确
const quick = walk("quick", () => 0);
if (!quick.finished) throw new Error("快速版没走到结果页");
out.quick = { steps: quick.steps, visited: quick.visited };

fs.writeFileSync(path.join(ROOT, "data", "js_results.json"),
  JSON.stringify(out, null, 2), "utf8");

console.log(`✓ JS 引擎走完 ${Object.keys(PICKERS).length} 条完整路径 + 1 条快速路径`);
console.log(`  完整版每题数：${Object.values(out.sets).map((s) => s.steps).join(" / ")}`);
console.log(`  快速版题数：${out.quick.steps}`);
for (const [name, s] of Object.entries(out.sets)) {
  console.log(`  ${name}: ${s.top.slice(0, 3).map((x) => x.en).join(" | ")}`);
}
