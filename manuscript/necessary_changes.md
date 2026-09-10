> 2026-09-09 更新：以下为此前版本记录。当前措辞精简和说明迁移以 `wording_cleanup_zh.md`、`supporting_methods_notes.md` 和当前 `main.tex` 为准；回复信已同步。

# 原稿底稿版：必要修改记录

此版由用户提供的原稿逐项修改生成，不以大幅修订稿的正文为底稿。
保留原稿标题、主要段落顺序、原有五段结论和大部分描述性句式。
保留已验证的图表排版修复；必要新增段落均对应明确审稿意见。

## 修改类别及依据

|序号|依据与必要性|修改后定位片段|
|---|---|---|
|1|排版：保留已验证的浮动体、英文字体和孤行控制设置|% main.tex -- International Journal of Remote Sensing manuscript \documentclass[]{interact} \us|
|2|R1.7 / R2.minor1 / R3.2：任务术语|Land Use/Land Cover (LULC) classification is essential|
|3|R3.2：分类不是变化模拟|scale of Earth observation data, accurately classifying LULC|
|4|R3.1 / R3.4：删除核心驱动力结论|has received increasing attention for LULC classification|
|5|R3.1 / R1.9：样本范围和名词用法|in this intersection, this study conducts an analysis of 261 publications|
|6|R3.1：摘要交代检索范围|integrating technical and bibliometric review methods. The search required both deep learning a|
|7|R3.1 / R3.4：不把增长外推或称指数增长|The number of published papers in this corpus has increased substantially since 2016|
|8|R3.1 / R3.4：检索设计不能证明技术转变|Research attention within the corpus centres on multi-source heterogeneous data fusion and deep|
|9|R1.3 / R3.4：条件性比较而非取代|The suitability of data-level, feature-level, and decision-level fusion depends on data alignme|
|10|R1.6 / R1.7：未来方向及术语|remote sensing foundation models, uncertainty-aware learning, and multimodal data governance te|
|11|R1.7 / R1.9：保留原关键词，仅统一任务和分隔符|Land-use and land-cover classification; deep learning; multi-source data fusion; feature fusion|
|12|R1.7 / R3.4：解释缩写并去除必然性|complementary modalities including light detection and ranging (LiDAR) and synthetic aperture r|
|13|R1.9：技术用词纠错|characterised by high spatial, temporal, and spectral resolutions|
|14|R3.2：统一分类对象|classification of complex land surfaces|
|15|R3.4：传统方法适用条件|While effective with suitable features and limited training samples, these shallow models may n|
|16|R3.4：避免绝对性能结论|which can limit their generalisation capabilities|
|17|R3.1：不宣称替代|has expanded the range of methods used in the field|
|18|R3.1 / R3.4：删除持续优于传统方法|Algorithms including Convolutional Neural Networks (CNNs) and the more recent Transformers can |
|19|R1.9：主谓一致|LiDAR data are often|
|20|R3.4：去除必然性|has been investigated as a strategy to improve LULC classification|
|21|R3.1 / R3.4：热度不等于主流|The intersection of deep learning and multi-source fusion has attracted increasing research att|
|22|R3.1：不把零记录早期描述成连续演化|remains relatively fragmented|
|23|R1.1：增加众包数据及质量限制| Sensor observations are not the only relevant information source. Crowdsourced geographic info|
|24|R1.9：避免无依据贬低既有综述|and may not cover subsequent developments|
|25|R1.7：架构不等于基础模型|Since their work predates Vision Transformers and state-space models like Mamba, it does not co|
|26|R3.4：计量指标不能衡量全球科研实力|Bibliometric analysis can complement these technical reviews by describing the geographical dis|
|27|R3.1：明确综述设计|This study conducts a bibliometric analysis and technical review|
|28|R1.9：删除不必要的排他性比较|This paper combines|
|29|R3.1 / R3.4：指标解释范围|map publication and citation patterns across countries, institutions, and authors in the retrie|
|30|R3.4：不假设技术更替|including CNN-based feature extraction and emerging trends such as Transformer and attention me|
|31|R1.3 / R1.5 / R3.4：比较目标纠正|compare the requirements, limitations, and suitable applications of different fusion strategies|
|32|R1.1：2026叙述补充边界|This study conducts a bibliometric analysis and technical review based on the Web of Science Co|
|33|R1.2 / R3.3：字段与索引，保留原段落结构|In the contemporary era, scientific literature datasets have become increasingly accessible to |
|34|R1.2 / R3.1 / R3.3：检索月份与范围|Considering that deep learning has emerged as a relatively recent research hotspot, the time sp|
|35|R1.2 / R2.minor2 / R3.3：保留检索表补充信息|\begin{table}[htb!] \centering \setlength{\belowcaptionskip}{5pt} \caption{Literature search st|
|36|R1.2 / R3.3：保留283→281→261及去重说明|During the data collection phase, literature retrieval was conducted using the Advanced Search |
|37|R3.1 / R3.4：方法目的限定|to describe publication trends and research hotspots within the retrieved LULC classification c|
|38|R1.2：软件版本|three specialised tools were employed: HistCite, VOSviewer version 1.6.20, and the Bibliometrix|
|39|R1.9：软件功能客观描述|HistCite provides statistical metrics, such as|
|40|R1.2 / R3.3：关键词、机构清洗、163与98篇、可审计材料|Currently, several software tools are available for the analysis and visualization of scientome|
|41|R2.minor3 / R3.4：年份与引文指标定义|The annual publication output reflects research activity within the retrieved corpus over time.|
|42|R2.minor3：零记录而非数量很少|because no publications were retrieved|
|43|R3.1：范围限定|the annual volume of publications in this corpus has exhibited|
|44|R3.4：相关趋势不能证明因果|This growth coincided with|
|45|R3.4：不将数量等同生产力|represent the peak publication counts|
|46|R3.1：自身统计不援引外部论文|papers published, respectively. This trend does not establish the share of fusion research in t|
|47|R3.4：限制指标解释|an indicator of research activity|
|48|R3.4：未检验统计显著性|are generally higher|
|49|R3.1：局部引文范围|within the selected corpus|
|50|R3.4：去除超出指标的价值判断|This is largely due to the work|
|51|R3.4：解释计量局限|Annual citation totals can be concentrated in a small number of papers and are affected by publ|
|52|R3.4：两指标峰值不同，不称一致|(1258).|
|53|R3.4：客观描述|contributed 345 global citations|
|54|R3.4：去除绝对影响力判断|Despite a very low publication count in 2016, the year achieved a high TGCS due to the work|
|55|R3.1 / R3.4：检索条件不能推出领域结论|Within this deliberately focused corpus, several highly cited studies concern the intersection |
|56|R3.4：保留直接支持引文时间窗的来源|\citep{bornmann2011citation}|
|57|R3.1：期刊结论限定|within the retrieved corpus|
|58|R3.4：删除未经分析验证的期刊因果解释|compared with its TGCS of 1246. These indicators use different citation populations; the observ|
|59|R3.4：指标不等于科研影响力|within the retrieved corpus.|
|60|R3.4：删除期刊声誉推断|although raw citation totals are influenced by publication age and a few highly cited papers.|
|61|R3.4：删除作者价值判断|This demonstrates his significant contribution to both the local community and global impact. |
|62|R3.4：无独立证据的影响力判断|The frequent collaboration between these two authors and others highlights their roles as influ|
|63|R3.4：只报告指标|Hong D. F. has the highest TGCS in the retrieved corpus|
|64|R3.4：机构作用描述|analysing the geographical distribution of publications|
|65|R3.1：机构范围|within the retrieved corpus|
|66|R3.4：未做显著性检验|exceeds that of the other listed institutions|
|67|R3.4：删除机构认可度推断|These results indicate that Wuhan University not only maintains high annual output but also com|
|68|R3.4：科研实力不由引文排名推出|have the highest TGCS values in the retrieved corpus|
|69|R3.4：国家指标解释|National contribution is another dimension for describing the geographical distribution of publ|
|70|R3.1 / R3.4：不外推研究重要性|within the retrieved corpus.|
|71|R3.4：不暗示已进行国家归一化分析|population size, research-system size, database coverage, and publication age can affect these |
|72|R3.1 / R3.4：删除绝对领先|China has the largest publication count in the retrieved corpus.|
|73|R3.4：单一国家署名不等于独立科研|The majority of China's records are single-country publications|
|74|R3.4：不推断网络实力|Collaborative links extend from China to countries in North America, Europe, and Australia with|
|75|R3.4：协作指标含义|India and Germany also show a high proportion of single-country publications.|
|76|R3.4：不称显著性|is more prominent.|
|77|R3.4：不由署名关系推断知识传播效果|these nations have international collaborative links. These patterns describe co-authorship in |
|78|R3.2：术语统一|261 publications related to LULC classification|
|79|R3.1 / R3.4：关键词不能证明技术演化|describes research topics and their temporal distribution in the retrieved corpus|
|80|R2.minor3：明确可视化时间范围|because no records were retrieved for 2006--2014 and only one for 2015|
|81|R1.8：与分面排版对应|(upper panel)|
|82|R3.1 / R3.2：范围与任务|the focus of the retrieved LULC classification research|
|83|R1.7：与节点标签一致|"land-cover classification"|
|84|R3.4：删除关键词推出技术演化|These terms indicate attention to multi-source data fusion and deep learning within the selecte|
|85|R1.8：与图中上下分面对应|(lower panel of Fig.~\ref{fig:keyword_evolution})|
|86|R3.4：删除未由时序图验证的四簇解释|several terms occur more frequently within the retrieved corpus.|
|87|R3.4：时序频次客观报告|were 104, 94, and 83|
|88|R3.4：节点连接不表示基础支撑|within the later-period network.|
|89|R3.1 / R3.4：限定关键词解释|indicating continuing attention within the retrieved corpus|
|90|R3.4：独立时间网络TLS可比性限制|According to the analysis of the 2021--2025 period (lower panel of Fig.~\ref{fig:keyword_evolut|
|91|R3.4：共现不是范式转移|indicates co-occurrence within this focused literature.|
|92|R3.4：节点位置不等于技术优越性|are also present within the network. Their presence indicates research attention, not superiori|
|93|R3.1 / R3.4：颜色含义与传统方法频次解释纠正|In contrast, nodes representing traditional methods, such as "support vector machines", "optica|
|94|R3.4：共被引定义|Co-citation analysis identifies documents cited together; it does not directly measure semantic|
|95|R3.4：不由簇直接推出知识演化|summarising groups of references cited together in the retrieved corpus|
|96|R2.minor5：作者数量纠正|Simonyan and Zisserman (2015, VGG)|
|97|R3.4：客观引用|work by Marmanis et al. (2016)|
|98|R3.4：不能由共被引证明方法取代|these methods support dense prediction and boundary delineation alongside patch-based classific|
|99|R3.4：簇不是作者支配关系|Including studies by|
|100|R3.4：共被引不证明起源链|Relevant work includes statistical modelling of sensor physics and evaluation frameworks for pi|
|101|R3.4：不把网络称范式转移|This cluster centres on|
|102|R3.4：模型机制替代宏观推断|This work uses self-attention for interactions between image tokens.|
|103|R1.7 / R3.4：Transformer架构不等于基础模型|papers such as Yao et al. (2023, ExViT), reflecting interest in long-range spatial modelling ra|
|104|R3.1：不预设DL领域主导|Prior to the widespread use of deep learning in the literature reviewed here,|
|105|R3.4：基线方法条件化|for small-sample and high-dimensional tasks, with performance depending on features and tuning.|
|106|R3.4：保留传统方法表的条件性描述|\begin{table}[!htbp] \centering \setlength{\belowcaptionskip}{5pt} \caption{Traditional methods|
|107|R3.3：保留163篇编码子集、98篇去向及分母限定|The archived second-stage content coding contains 163 records with an explicit and classifiable|
|108|R3.1 / R3.4：删除密度证明主导|As shown in the keyword density visualisation (Fig.~\ref{fig:keyword_density}), the highest-den|
|109|R2.major2：基准实验并不必然稳健|the evaluation of these deep learning fusion models relies heavily on benchmark datasets.|
|110|R3.1：数据集频次范围|were the most prevalent benchmarks in the included corpus.|
|111|R2.major2：补充benchmark代表性限制|Currently, the evaluation of these deep learning fusion models relies heavily on benchmark data|
|112|R2.minor4 / R3.5：保留多模态数据集与参数纠正|\begin{table}[!htbp] \centering \setlength{\belowcaptionskip}{8pt} \caption{Technical specifica|
|113|R1.7 / R3.5：数据集名称|Houston and MUUFL Gulfport|
|114|R3.5：图表选择范围及来源|As evidenced by the technical specifications in Table~\ref{tab:datasets_detail}, the integratio|
|115|R1.3 / R3.4：融合层级不是递进阶段|three levels: Data-level Fusion, Feature-level Fusion, and Decision-level Fusion|
|116|R1.3 / R1.5 / R3.4：混合融合与非递进关系|These are alternative integration choices rather than a mandatory progression. Hybrid fusion co|
|117|R1.5：保留融合层级比较表、解释和公平比较约束|\begin{figure}[!ht] \centering \includegraphics[width=1.0\columnwidth, trim=0 10 0 10, clip]{Fi|
|118|R1.7：统一融合层级标题|\subsection{Data-Level Fusion}|
|119|R1.3 / R1.7：区分原始点云与共配准输入|Data-level fusion, often referred to as pixel-level or raw-level fusion, involves the direct in|
|120|R3.4：关键词客观描述|occur frequently in the retrieved corpus|
|121|R3.4：词频不能证明技术转移|studies investigate the synergy of these sensors to address individual spectral or structural l|
|122|R1.3：传感器能力纠错|which can complement optical imagery from sensors like Sentinel-2; cloud-penetrating observatio|
|123|R1.3 / R3.4：保留瓶颈与模型输入讨论，删除必然优越性|Despite its foundational importance, data-level fusion faces persistent technical bottlenecks, |
|124|R1.3 / R3.4：避免无条件快速收敛|Inductive bias for local texture/edge capture.|
|125|R1.3：CNN限制条件|Local receptive field; long-range interaction requires additional depth or modules.|
|126|R3.4：技术方向而非替代路径|Hybrid CNN-Transformer architectures.|
|127|R1.3 / R3.4：注意力能力不等于必然优势|Direct interaction between tokens; can support cross-modal fusion.|
|128|R1.3：复杂度适用范围|Dense attention has quadratic token-pair cost; data demand is task-dependent.|
|129|R3.4：删除普遍SOTA判断|Efficient variants (Swin, SoftFormer).|
|130|R1.3：注意力条件性及解释性|Can emphasise task-relevant features; weights are not necessarily explanations.|
|131|R1.3：注意力不自动解决配准|Cross-modal attention; alignment still requires evaluation.|
|132|R2.major1：效率取决实现|Sequence and long-range modelling.|
|133|R2.major1：理论与端到端成本|Theoretically linear sequence scaling; total cost is implementation-dependent.|
|134|R2.major1：真实证据限制|Early stage; limited 2D multimodal and cross-region validation.|
|135|R1.1：移除不直接支持Mamba的基础模型引用，文中仍保留该论文|\citep{5,49,53}|
|136|R3.4：不存在普遍最优平衡|with a balance between information preservation and computational efficiency that depends on th|
|137|R3.1：限定关键词范围|Within the retrieved corpus, bibliometric analysis reveals that "CNN",|
|138|R3.4：删除技术生态基础判断|DL provides|
|139|R3.1 / R3.4：频次不是主流证据|reducing dependence on manual feature engineering. This supports the use of feature-level fusio|
|140|R1.9：数与冠词|CNNs served as core tools|
|141|R1.3 / R3.4：能力条件化|They are designed to capture local spatial features|
|142|R3.4：不作普遍显著改进|CNNs can improve classification accuracy, depending on data alignment, training, and evaluation|
|143|R3.1 / R3.4：研究关注度范围|This architecture has attracted increasing attention in the retrieved literature.|
|144|R1.9：区分发表年与引文统计时点|The 2023 study|
|145|R3.4：引文观测时点|had a TGCS of 312 at the time of data collection.|
|146|R1.3 / R3.4：去除未经验证的具体尺度外推|Transformers can capture long-range spatial dependencies beyond local convolutional receptive f|
|147|R1.3：机制客观化|learns data-dependent weights|
|148|R1.3：补充解释性及验证要求|Feature Extraction and Attention Mechanisms: These represent the core technical phases of fusio|
|149|R3.4：缺少最常用统计|This is an application scenario for feature fusion.|
|150|R1.3 / R3.4：替换泛化效果陈述|with results dependent on resolution, label definitions, and evaluation design|
|151|R2.major1：Mamba未证实|its role as a backbone for LULC fusion remains under evaluation.|
|152|R2.major1 / R3.4：复杂度变量与非优越性|Dense Transformer self-attention permits long-range interaction, but its pairwise interaction c|
|153|R2.major1：理论复杂度不等于实际效率|with theoretically linear scaling in sequence length; end-to-end cost also depends on spatial s|
|154|R2.major1：准确率效率瓶颈不能声称解决|illustrate Mamba's feasibility, not a demonstrated solution to the accuracy-efficiency trade-of|
|155|R2.major1：具体待验证条件|requires further empirical validation across 2D multimodal, cross-region, and cross-sensor sett|
|156|R1.3 / R3.4：非线性替代|These approaches offer different local, long-range, and computational properties; their relativ|
|157|R1.7：层级一致|\subsection{Decision-Level Fusion}|
|158|R3.2：决策融合任务术语|independent classification outputs|
|159|R1.3：采用遥感决策融合来源|\citep{55}|
|160|R3.1 / R3.3 / R3.4：频次范围与性能区分|it occurs less frequently than feature-level approaches in the archived fusion-content subset, |
|161|R1.3：决策融合条件性限制|it may not capture low-level complementary relationships and cross-modal correlations available|
|162|R1.3：保留信息解耦主线，补充模块化、校准与缺失模态约束|The primary limitation of decision-level fusion lies in its "information decoupling" nature: by|
|163|R1.1 / R1.4 / R2.major3：学习策略、基础模型和近期文献|\subsection{Learning Strategies Beyond Architecture Design} Architecture choice is only one com|
|164|R3.4：词频描述|occur frequently in the retrieved corpus|
|165|R3.4：词频不等于忽视问题|This contrast motivates discussion of data reliability, although keyword frequency does not mea|
|166|R1.9 / R2.major2：新增挑战条目|associated with the data in four aspects|
|167|R1.3 / R3.4：不宣称Transformer普遍更敏感|Errors in raw data can be propagated or amplified by deep learning models|
|168|R1.1：审稿人建议的土地利用不确定性文献|leading to distorted classification results. Uncertainty in land-use inputs can also affect dow|
|169|R1.3 / R2.major2：具体失败条件|Residual sub-pixel offsets and acquisition-time differences|
|170|R2.major2：时序错配评价|may trigger "pseudo-change" misinterpretations. Acquisition dates, registration accuracy, resam|
|171|R2.major2：类别不平衡|\textbf{Scarcity and Imbalance of High-Quality Annotations:}|
|172|R2.major2：类别不平衡评价|limiting applications in large-scale scenarios. Rare classes and inconsistent label taxonomies |
|173|R2.major2：增加小基准向大区域迁移的限制|\item \textbf{Limited benchmark representativeness:} Houston, Trento, MUUFL Gulfport, Berlin, a|
|174|R1.3 / R2.major2：效率与部署条目|algorithms into four aspects, setting the stage for the subsequent discussion of potential reme|
|175|R1.3：避免化学/物理的错误二分|the spectral features|
|176|R1.3：避免化学/物理的错误二分|the structural features|
|177|R3.4：不宣称简单拼接是主流|Simple channel concatenation or weighted summation does not itself provide adaptive feature ali|
|178|R1.3：解释性不以普遍高精度为前提|CNNs and Transformers are often viewed as black boxes.|
|179|R3.2：分类解释不是变化因果|different modalities to LULC predictions|
|180|R1.3 / R2.major3：解释性与校准|weakening the persuasiveness of geographical explanations. Modality ablation, counterfactual ma|
|181|R2.major2 / R3.4：不能把随机划分等同独立验证|Random within-scene training/test splits do not establish generalisation to new regions.|
|182|R2.major2：跨域检验|hindering the goal of "train once, apply globally". Geographically and temporally disjoint test|
|183|R1.3 / R2.major1：端到端效率与部署|\item \textbf{Efficiency and operational constraints:} Model size, memory use, latency, energy |
|184|R1.10：保留开放科学和仓库说明|\section{Reproducibility and Open Science} Supporting materials for this review are available a|
|185|R3.1 / R3.2：综述任务|to review the application of deep learning (DL) and multi-source data fusion in LULC classifica|
|186|R3.1 / R3.4：增长范围与非指数性|Analysis of 261 publications reveals that since 2016, publication activity has increased within|
|187|R3.1 / R3.4：核心范围限制|Because the search required both deep learning and fusion terms, it cannot establish that deep |
|188|R3.4：国家指标含义|China and Germany rank among the top three countries by publication count, TLCS, and TGCS withi|
|189|R3.1：没有无fusion对照语料|describes research on heterogeneous multi-source fusion within the selected corpus.|
|190|R3.4：特征融合不是普遍最稳健|offers one strategy whose suitability depends on alignment, sample availability, computation, a|
|191|R3.3 / R3.4：编码分母与架构并存|We observed attention to both the local feature-centric approach of CNNs and global context-awa|
|192|R2.major1：结论Mamba条件化|offers theoretically favourable sequence scaling, but its 2D multimodal and cross-region perfor|
|193|R3.4：无跨研究统一性能排名|Despite advances in model design,|
|194|R3.2：分类不是模拟|"pseudo-changes" in fused observations.|
|195|R3.4：无需SOTA标签|current models|
|196|R1.9 / R2.major2：语法与外推限制|regions where ground-truth data are scarce. Small benchmark datasets do not by themselves valid|
|197|R1.6：方向性建议|the integration of Explainable Artificial Intelligence (XAI) is important.|
|198|R1.6 / R3.4：XAI不是因果保证|can help researchers quantify|
|199|R1.4 / R1.6：零样本不是微调，避免保证全球稳健|large-scale foundation models may support few-shot adaptation or zero-shot transfer, but their |
|200|R1.6：必要未来方向且不保证消除噪声|This can help multi-source fusion use "model-ready" data while limiting spatiotemporal inconsis|
|201|R3.4：不作新时代判断|has expanded the available approaches for LULC classification.|
|202|R1.6：未来建议条件性|Such advancements can provide|
|203|R1.8 / R2.minor3：保留图像布局、图注与任务限定|\begin{figure}[htb!] \centering \includegraphics[width=0.9\linewidth]{Figures/flowchart.pdf} \c|
|204|R1.8 / R2.minor3：保留图像布局、图注与任务限定|\begin{figure}[htb!] \centering \includegraphics[width=0.75\columnwidth]{picture_2.png} \captio|
|205|R1.8 / R2.minor3：保留图像布局、图注与任务限定|\begin{figure}[htb!] \centering \includegraphics[width=0.67\columnwidth]{Figures/Picture_3.pdf}|
|206|R1.8 / R2.minor3：保留图像布局、图注与任务限定|\begin{figure}[htb!] \centering \includegraphics[width=0.67\columnwidth]{Figures/Picture_4.pdf}|
|207|R1.8 / R2.minor3：保留图像布局、图注与任务限定|\begin{figure}[!htbp] \centering \includegraphics[width=0.67\columnwidth]{Figures/Picture_5.pdf|
|208|R1.8 / R2.minor3：保留图像布局、图注与任务限定|\begin{figure}[!htbp] \centering \includegraphics[width=0.67\columnwidth]{Figures/Picture_6.pdf|
|209|R1.8 / R2.minor3：保留图像布局、图注与任务限定|\begin{figure}[htb!] \centering \includegraphics[width=1.0\textwidth, height=0.38\textheight, k|
|210|R1.8 / R2.minor3：保留图像布局、图注与任务限定|\begin{figure}[!htbp] \centering \includegraphics[width=0.98\linewidth]{Figures/picture_9.pdf} |
|211|R1.8 / R2.minor3：保留图像布局、图注与任务限定|\begin{figure}[!htbp] \centering \includegraphics[width=1.0\columnwidth]{Figures/new_Relitu.pdf|
|212|R1.8 / R2.minor3：保留图像布局、图注与任务限定|\begin{figure}[!htbp] \centering \includegraphics[width=1.0\columnwidth]{Figures/top_datasets_r|
|213|R1.8 / R2.minor3：保留图像布局、图注与任务限定|\begin{figure}[!htbp] \centering \includegraphics[width=1.0\columnwidth, trim=0 10 0 10, clip]{|
|214|R1.8：保留关键词图放大分面，不重算节点|\begin{figure}[!htbp] \centering \subfloat[2016--2020]{% \includegraphics[ width=0.96\linewidth|
|215|R1.8：长引文移到表下注释，保留原表各列与局部纠错|\begin{table}[htb!] \centering \setlength{\belowcaptionskip}{5pt} % 提示：配合导言区的 captionsetup，这里的标|

## 回复信需要同步的文字

- 标题恢复原稿的 Technological evolution trajectory and future trends；回复信封面 Revised title 应采用同一标题。
- 第3节恢复原稿标题 Basic Situation Analysis；回复信中的 Bibliometric Profile 定位应改为此名称。
- 结论沿用原五段结构进行局部必要修改，回复信不宜再写整节重写，可写“revised the conclusion to qualify the main findings and make the research recommendations more specific”。
- Table 5 保留原列结构并作局部纠错；长参考文献移到表下注释。
- 回复信的其余实质性回应仍需以最终源文和具体审稿条目为准；本次未改检索、编码数据或Github状态。
- 此版未解决未核实的历史设置或数据来源问题；已有透明度说明保留，不增造历史信息。
