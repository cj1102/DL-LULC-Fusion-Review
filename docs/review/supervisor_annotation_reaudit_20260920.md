# 教师批注复核记录（2026-09-20）

## 本次修正

摘要首句已按用户本次要求删除 essential，并作必要的语法衔接，现为：

> Land Use/Land Cover (LULC) classification aids understanding of human-environment interactions and ecological impacts and supports sustainable land management.

本次正文只改这一句。此前缩短的Conclusion、图8—11图注、4.7节过渡、表4引用位置、英国英语拼写及Land Use/Land Cover写法均保留。4份工作源文件内容一致。按用户要求不编译或更新论文PDF、diff PDF、回复信及源码ZIP。

## 复核范围与结论

重新读取原始批注文件 `manuscript_original_baseline_revised(1).pdf` 的全部33页批注对象，并重新渲染全部页面，逐页筛查可见标记；对含批注的第1、2、3、21、22页作完整页面核对。共找到32处编辑标记：18处高亮、10处删除线、2处文字框、2处下划线，其中17处含文字意见。没有找到其他可见的编辑标记。

这份原PDF的摘要 essential 处没有可见标红或删除线，也没有对应批注对象；本次以用户明确要求为依据落实删除，不把这一要求虚记为原PDF已有的第33处批注。

原PDF中的10处红色删除线均已落实。此前记录的28项定点改动逐一与当前源码核对，均仍存在；其中“in this corpus”删除与时间范围调整按最终完整句核对，避免将中间版本误判成未修改。

以下事项不能笼统表述为“全部原样落实”：

- 4处无替换文字的标记（are、relative to traditional methods、术语关系句、Topic field (TS)）保留，理由列于下表；这不表示已确认老师同意保留。
- “Experimental”按综述性质采用“The results”；“WoS”按正文已定义的缩写采用“WoSCC”。这2处是适配后的处理。
- 用户后来提及的“将流程图拆分并放入Discussion”尚未实施；独立示意图方案不等于正文已调整。

## 原PDF逐项对照

下表行号对应当前 `manuscript/main.tex`，页码和编号来自原批注PDF。

| 原PDF页码 | 标记编号 | 标记/意见 | 当前处理 | 落实及说明 | 源码行号 |
|---|---|---|---|---|---|
| 1 | 2973 | 摘要LULC写法 | 已满足 | 已统一为用户指定的 Land Use/Land Cover (LULC)，本轮保持。 | 53 |
| 1 | 2977 | 引言LULC写法 | 已满足 | 与摘要、标题和关键词一致，本轮保持。 | 63 |
| 1 | 2984 | 删除 published | 已修改 | 删除 publications 后重复的 published。 | 53 |
| 1 | 2988 | 删去摘要检索范围说明 | 已修改 | 删除被划去的整句；摘要仍明确261篇及2006—2025，检索式与方法部分仍说明研究范围。 | 53 |
| 1 | 2992 | Our → Experimental | 按研究类型调整 | 采用 The results，消除第一人称；本文为综述，不能将这些结论称作 Experimental results。 | 53 |
| 1 | 2996 | 删除 in this corpus | 已修改 | 按批注删除摘要中这处重复限定。 | 53 |
| 1 | 3000 | since 2016 → from … to … | 已修改 | 写为 from 2016 to 2025，与统计截止年份对应；封闭时间段使用一般过去时 increased。 | 53 |
| 1 | 3004 | 删除 within the corpus | 已修改 | 按批注删除摘要中这处重复限定。 | 53 |
| 1 | 3012 | 引言首段加2篇参考文献 | 已修改 | 分别补引 Ghamisi et al. (2019) 与 Ma et al. (2019)；用 respectively 明确LiDAR结构信息与SAR全天候观测的对应。 | 63 |
| 2 | 3014 | 跨页高亮延续 | 已修改 | 该标记延续上一页首段批注，已在分类挑战句补引 Ma et al. (2019)。 | 63 |
| 2 | 3028 | 传统机器学习段参考文献偏少 | 已修改 | 在SVM/RF介绍后补引 Belgiu and Drăguţ (2016)，在特征工程局限句后补引 Ma et al. (2019)。 | 66 |
| 2 | 3032 | 多源融合段参考文献偏少 | 已修改 | 在单源局限句后补引 Ghamisi et al. (2019)，在多模态分类句后补引 Hong et al. (2021)。 | 69 |
| 2 | 3034 | 高亮 are，无替换文字 | 已检查并保留 | data 在此采用学术英语复数用法，are 与主语一致；不凭高亮擅自改成 is。 | 69 |
| 2 | 3038 | 补充 However, | 已修改 | 使用 However, despite the growth in publications, …，明确转折并保留原来的让步条件。 | 69 |
| 2 | 3042 | 高亮 relative to traditional methods | 已检查并保留 | 保留比较对象和性能依赖条件；没有明确替换或删除指令。 | 66 |
| 2 | 3046 | The → This | 已修改 | 按批注改为 This intersection，与前句所述融合衔接。 | 69 |
| 2 | 3050 | 传感器与众包信息两句关联 | 已修改 | 合为 In addition to sensor observations, crowdsourced geographic information can provide …。 | 72 |
| 2 | 3054 | 术语关系句下划线 | 已检查并保留 | 前文已区分multi-source fusion与multimodal learning，保留这句概念说明；没有删除指令。 | 72 |
| 2 | 3059 | the field’s → its | 已修改 | 按批注使用 its evolution。 | 74 |
| 3 | 3063 | 2026年文献说明脱节 | 已修改 | 并入研究目标段，用 technical discussion 承接定性技术讨论，明确2026年文献为叙述补充、不进入2006—2025计量统计。 | 77 |
| 3 | 3067 | 删除 In the contemporary era | 已修改 | 删除冗余开头，并将 Scientific 首字母大写。 | 83 |
| 3 | 3071 | Considering that → Since | 已修改 | 按批注替换连接词。 | 85 |
| 3 | 3075 | 261篇筛选结果引用图1 | 已修改 | 补入 Fig.~\ref{fig:flowchart}，保持自动编号。 | 85 |
| 3 | 3079 | 导出格式和search settings合句 | 已修改 | 以逗号和 and the search settings 连接，保留导出格式原文。 | 85 |
| 3 | 3083 | 写明bibliometric analysis具体方法 | 已修改 | 括号补充发表与引文统计、共词、合著和共被引分析，与后文实际方法一致。 | 124 |
| 3 | 3087 | Web of Science → WoS | 按现有缩写调整 | 采用当前稿件已定义的 WoSCC，落实避免重复全称的要求，不再引入未定义的WoS。 | 126 |
| 3 | 3091 | 高亮 Topic field (TS) | 已检查并保留 | 2.1已说明TS覆盖题名、摘要、作者关键词和Keywords Plus，2.2保持相同写法；没有替换文字。 | 126 |
| 3 | 3095 | Because → Since | 已修改 | 按批注替换连接词。 | 126 |
| 3 | 3099 | 删除 therefore | 已修改 | 删除该句冗余连接词，筛选数字保持不变。 | 126 |
| 21 | 3008 | SAR全称重复 | 已修改 | 4.4直接使用SAR；引言首次出现的全称及定义保留。 | 416 |
| 22 | 3103 | 删除CNN重复全称 | 已修改 | 4.5标签改为 CNN:，保留原段落内容。 | 457 |
| 22 | 3107 | 删除Deep Learning重复全称 | 已修改 | 4.5标签改为 DL:，同时正确去掉括号，保留原段落内容。 | 454 |
