# 原稿底稿修订源包（说明更新于2026-09-20）

2026-09-20同步：39页diff由未改写的 `original_main.tex` 与当前 `main.tex` 重新生成；14页回复信已对应当前源码更新。结论采用作者刚确认的保留句式、小幅删减版本。此次同步没有改动 `main.tex` 内容。

正文源码包含老师批注对应的文字修改、图8—11图注、表4引用位置及已确认的过渡调整。表4完整收录在回复信第6页，Vaswani引用移至表下注释。未来可复现性建议位于GitHub的 `TODO.md`。图1的箭头、黑色边框及标签对齐调整已包含在当前图文件中；将流程图拆分并放入Discussion尚未实施。

源ZIP已更新，包含当前正文、diff及编译依赖。按作者要求，干净版正文PDF未重新编译；请以当前 `main.tex` 手动编译，已有33页正文PDF不代表本次源码。回复信以章节、图号和表号定位，不使用旧页码。

## 编译与文件

- `main.tex`：当前正文，按作者要求由作者手动编译修改版PDF。
- `main_diff.tex`：与原稿比较的差异稿，编译后39页。
- `main_diff_references.tex`：差异稿必须保留的参考文献对照文件，与 `main_diff.tex` 放在同一目录。
- `interactapasample.bib`：已校正的当前参考文献库。
- `original_main.tex`、`original_references.bib`：从同一用户原稿ZIP留存的原始正文和文献库，未改写。
- `original_for_diff.tex`：比较用中间稿，统一等价引号，并为已变更或删除的引文设原版别名；不作为单独主文件编译，也不是另一份原稿。
- `Figures/`、`picture_2.png`、`.cls` 和 `.sty`：编译依赖。
- `supporting_methods_notes.md`：与正文相配套的方法与归档说明。

使用Tectonic或常规LaTeX/BibTeX工作流编译。Tectonic命令示例：`tectonic --keep-logs --keep-intermediates main.tex`；差异稿将文件名换为 `main_diff.tex`。不要单独复制 `main_diff.tex` 而漏掉 `main_diff_references.tex`。

## 对照原则

红色表示原稿删除内容，蓝色表示新增内容。正文通常使用删除线和波浪线；部分整行表格及参考文献采用红蓝颜色区分。旧引文保留原始作者和年份，避免文献库更新后旧引文被自动显示成新版本。参考文献列表同时展示发生变化的旧、新条目。

比较统一等价编码，显示纯大小写变化，忽略部分排版控制；未变更的标题跨越其自身浮动表格的位置调整不重复标注。实质性文字变化保留。图像展示当前版本，不提供像素差异。因此diff是文字、表格及参考文献对照，不是完整文件字节差异。

原稿SHA-256：`cd8f80e6288f781aebf309b54c8dcf444f2c93a0d365c852780f24b9b4a6e77c`。

## 保留与修正范围

保持英式英语，尽量沿用原稿句式，仅保留回应审稿意见及修正事实、引用、语法所需的调整。4.2保留作者确认的共被引设置（association-strength、resolution 1.00、minimum cluster size 1）与图例说明；4.7开头保留过渡。表2主要措辞和两句被引评价保留必要限定。

修订包括参考文献、数据集参数及少量论据位置的校正。论文结果按当前正文报告。

当前LaTeX、39页差异稿、源包及14页回复信已同步；已有干净版PDF仍是此前编译版本。当前261篇名单与公开输入已经按UT逐条对应，说明见GitHub的 `docs/coding_sheet_omissions.md`。回复信第6页完整收录新增表4。

2026-09-15术语复核按作者指定格式统一为 `Land Use/Land Cover (LULC)`，并同步缩写全称、术语拼写及回复信。正式文献题名和检索字符串保留原样。大小写变化现在也在diff中标注。

## 历史记录

`necessary_changes.md`、`revision_scope_zh.md`、`wording_cleanup_zh.md`、`minimal_revision_round2_zh.md`、`table_and_citation_restore_zh.md`、`final_seven_restorations_zh.md` 保留此前修订过程，里面的页码、待确认事项和同步状态可能已经过时。以本README、`submission_audit_zh.md` 及当前正文为准。
