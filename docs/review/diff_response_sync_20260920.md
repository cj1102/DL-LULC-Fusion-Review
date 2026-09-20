# diff及回复信同步记录（2026-09-20）

本次以提交 `6e03e9f` 中的 `main.tex` 为固定版本，未改动正文。结论是作者确认的保留原有句式、仅做小幅删减版本。diff仍与最初留存的 `original_main.tex` 比较，不以中间改写稿作为底稿。

## 当前文件

- `manuscript/main.tex`：当前正文源码，SHA-256为 `c252de1963de7877ecd697b212682f49cec078011bbaa2718d576c3510f3a9c2`。
- `manuscript/main_diff.tex`及配套参考文献文件：重新生成，编译为39页 `manuscript_diff.pdf`。
- `docs/review/response_to_reviewers_original_baseline_aligned.docx`：14页，23条审稿意见原文及结构保留；表4位于第6页。
- `manuscript/manuscript_original_baseline_source.zip`：当前源码与依赖，逐文件核对通过。
- `manuscript/manuscript_revised.pdf`：此前33页干净版，未重新编译。作者应从当前源码手动编译正文PDF。

## 回复同步位置

| 对应意见 | 同步内容 |
|---|---|
| R1.1 | 2026年文献用于技术讨论，计量语料仍为2006–2025；不再声称正文保留已删除的引言说明句。 |
| R1.2、R3.3 | 图9—11均按作者确认报告association-strength、resolution 1.00、minimum cluster size 1；归档说明补记后续确认。 |
| R1.5 | 表4中Vaswani引用移入表下注释，保留表格内容及原生公式。 |
| R1.6 | 结论说明对应保留句式、小幅删减，保留结论范围及研究建议。 |
| R1.8 | 图8国家底色和蓝线含义，以及图9平均年份、图10关键词聚类、图11共被引聚类的区别。 |
| R1.10 | 未来报告清单位于GitHub TODO.md，不再声称完整清单仍在正文第6节。 |
| R2.major3 | 4.7开头从融合层级、架构转向学习策略的过渡。 |

## 核查

原稿和当前正文指纹均保持不变；独立目录重建diff得到相同文件；接受修订后的正文词项集合一致，剔除浮动图位置后正文与表格词序一致。diff编译无未定义引用或Overfull警告。已检查diff页面与结论、表4重点页面，并逐页检查14页回复信。此次核查针对文件同步和排版，不代表重新计算统计或重新开展文献事实核查。流程图拆分放入Discussion仍未实施。
