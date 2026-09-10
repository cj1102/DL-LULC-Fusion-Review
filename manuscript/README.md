# 原稿底稿修订源包（2026-09-10）

**当前状态：全文检查及明确错误修正完成；等待作者原始261篇统计结果完成数据对齐，尚未通过投稿前最终核验。** 已修正问题、待核对统计和参考来源见 `submission_audit_zh.md`。

## 编译与文件

- `main.tex`：当前正文，设为主文件可编译33页修改版。
- `main_diff.tex`：与原稿比较的差异稿，编译后38页。
- `main_diff_references.tex`：差异稿必须保留的参考文献对照文件，与 `main_diff.tex` 放在同一目录。
- `interactapasample.bib`：已校正的当前参考文献库。
- `original_main.tex`、`original_references.bib`：从同一用户原稿ZIP留存的原始正文和文献库，未改写。
- `original_for_diff.tex`：比较用中间稿，统一等价引号，并为已变更或删除的引文设原版别名；不作为单独主文件编译，也不是另一份原稿。
- `Figures/`、`picture_2.png`、`.cls` 和 `.sty`：编译依赖。
- `supporting_methods_notes.md`：详细方法与归档说明；其中统计关系仍需按原始261篇核对。

使用Tectonic或常规LaTeX/BibTeX工作流编译。Tectonic命令示例：`tectonic --keep-logs --keep-intermediates main.tex`；差异稿将文件名换为 `main_diff.tex`。不要单独复制 `main_diff.tex` 而漏掉 `main_diff_references.tex`。

## 对照原则

红色表示原稿删除内容，蓝色表示新增内容。正文通常使用删除线和波浪线；部分整行表格及参考文献采用红蓝颜色区分。旧引文保留原始作者和年份，避免文献库更新后旧引文被自动显示成新版本。参考文献列表同时展示发生变化的旧、新条目。

比较统一等价编码，忽略纯大小写差异和部分排版控制；未变更的标题跨越其自身浮动表格的位置调整不重复标注。实质性文字变化保留。图像展示当前版本，不提供像素差异。因此diff是文字、表格及参考文献对照，不是完整文件字节差异。

原稿SHA-256：`cd8f80e6288f781aebf309b54c8dcf444f2c93a0d365c852780f24b9b4a6e77c`。

## 保留与修正范围

保持英式英语，尽量沿用原稿句式，仅保留回应审稿意见及修正事实、引用、语法所需的调整。4.2保留作者确认的共被引设置（association-strength、resolution 1.00、minimum cluster size 1）与图例说明，位于正文第15页；4.7过渡位于正文第24页。表2主要措辞和两句被引评价保留必要限定。

本轮校正参考文献、数据集参数及少量论据位置，未重算文献计量数据，未改动图像资产。年度数量、排名、语料来源及网络输入仍待作者原始261篇资料核验。

正文、差异稿、源包及回复信在本地同步，并按作者要求纳入本轮GitHub发布；统计核对继续单独进行。当前261篇名单与公开输入已经按UT逐条对应；这不等于历史统计结果均已一致。说明详见GitHub的 `docs/coding_sheet_omissions.md`。线上发布状态以仓库提交记录及本地发布核验记录为准。

## 历史记录

`necessary_changes.md`、`revision_scope_zh.md`、`wording_cleanup_zh.md`、`minimal_revision_round2_zh.md`、`table_and_citation_restore_zh.md`、`final_seven_restorations_zh.md` 保留此前修订过程，里面的页码、待确认事项和同步状态可能已经过时。以本README、`submission_audit_zh.md` 及当前正文为准。
