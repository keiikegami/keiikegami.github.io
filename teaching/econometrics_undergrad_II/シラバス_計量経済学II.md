# 計量経済学II 授業計画

## 講義概要

本講義では、計量経済学の応用として、実証産業組織論と quantitative marketing の基礎を学ぶ。価格、商品属性、広告、キャンペーン、など、企業や政策当局が実際に直面する意思決定を題材に、データから需要、代替性、施策効果、顧客価値をどのように推定し、どのように意思決定に結びつけるかを考える。また、その過程で計量経済学の基本的な推定方法や識別のアイディアを学ぶ。

前半では、logit、nested logit、random coefficient logit などの離散選択モデルを用いて、需要推定、価格弾力性、代替性、合併分析を扱う。後半では、コンジョイント分析、A/Bテスト、広告・販促施策の因果効果測定、消費者異質性、顧客パネルデータ、動学的離散選択、ターゲティング、dynamic pricing を扱う。

15回のうち、通常講義を13回、ゲスト講義を2回予定する。需要推定の学習後に公正取引委員会の実務に関するゲスト講義を行い、後半では民間企業でのエコノミスト経験を持つゲスト講師による講義を行う。

## 到達目標

- 離散選択モデルを用いた需要推定の基本的な考え方を説明できる。
- 価格弾力性、代替性、商品属性への支払意思額を、企業・政策の意思決定と結びつけて理解できる。
- マーケティング施策の効果測定において、予測、相関、因果効果を区別できる。
- A/Bテスト、DiD、IV、RDD、固定効果モデルなどの識別戦略を、実務上の問いに応じて使い分ける視点を身につける。
- 顧客パネルデータから潜在的な消費者異質性や離脱リスクを推定する考え方を理解できる。
- 顧客価値の予測と、施策配分のための因果効果・政策評価を区別できる。
- 需要推定、顧客分析、ターゲティング、価格最適化が、それぞれ何を推定し、どのような仮定に依存しているかを説明できる。

## 前提知識

回帰分析、操作変数法、固定効果モデル、因果推論の基礎を前提とする。行列計算、最尤法、GMM、離散選択モデル、ベイズ推定については講義内で必要に応じて復習する。

## 主教材・参考文献

主教材：

- （主教材）上武康亮・遠山祐太・若森直樹・渡辺安虎『実証ビジネス・エコノミクス』日本評論社、2025年。

補助教材：

- （補助教材・離散選択）Train, Kenneth E. (2009) *Discrete Choice Methods with Simulation*, 2nd ed., Cambridge University Press.
- （補助教材・A/Bテスト）Kohavi, Ron, Diane Tang, and Ya Xu (2020) *Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing*, Cambridge University Press.

各回の追加文献は下記に示す。

## 授業計画・リーディングリスト

### 第1回　計量経済学の応用としての実証産業組織論/quantitative marketing

講義全体の地図を示し、需要推定、因果推論、顧客分析、価格最適化がどのように企業・政策の意思決定に結びつくかを整理する。次回からは、その土台として離散選択モデルを学ぶ。

講義内容：

- 実証ビジネス・エコノミクス、実証産業組織論、quantitative marketing の関係を整理する。
- 価格、広告、商品設計、顧客価値をデータで分析するとはどういうことかを概観する。
- 予測、因果効果、反実仮想の違いを確認する。

Reading：

- （主教材）上武ほか『実証ビジネス・エコノミクス』第1章。
- （サーベイ）Chintagunta, Pradeep, Tulin Erdem, Peter E. Rossi, and Michel Wedel (2006) "Structural Modeling in Marketing: Review and Assessment," *Marketing Science*, 25(6), 604-616.
- （実務・技術企業）Athey, Susan and Michael Luca (2019) "Economists (and Economics) in Tech Companies," *Journal of Economic Perspectives*, 33(1), 209-230.
- （計量・統計の視点）Einav, Liran and Jonathan Levin (2014) "Economics in the Age of Big Data," *Science*, 346(6210), 1243089.

### 第2回　離散選択モデル1：logitで需要を考える

前後とのつながり：第1回の概観を受けて、消費者の選択をモデル化する最初の道具として logit を導入する。次回は、この基本モデルの限界である代替性と価格内生性に進む。

講義内容：

- 消費者が複数の商品から1つを選ぶ状況を random utility model として表す。
- multinomial logit、outside option、choice probability を導入する。
- 価格弾力性と需要予測がプライシングにどう使われるかを学ぶ。

Reading：

- （主教材）上武ほか『実証ビジネス・エコノミクス』第2章。
- （教科書・離散選択）Train, Kenneth E. (2009) *Discrete Choice Methods with Simulation*, 2nd ed., Cambridge University Press, Chapters 2-3.
- （基礎理論）McFadden, Daniel (1986) "The Choice Theory Approach to Market Research," *Marketing Science*, 5(4), 275-297.
- （実証・ブランド選択）Guadagni, Peter M. and John D. C. Little (1983) "A Logit Model of Brand Choice Calibrated on Scanner Data," *Marketing Science*, 2(3), 203-238.
- （計量・統計の視点）Manski, Charles F. (1977) "The Structure of Random Utility Models," *Theory and Decision*, 8(3), 229-254.

### 第3回　離散選択モデル2：代替性と価格内生性

前後とのつながり：第2回の logit を出発点に、IIA による代替性の制約と、価格が需要ショックと相関する内生性の問題を扱う。次回は、消費者異質性を入れた需要推定と合併分析へ進む。

講義内容：

- logitモデルにおける IIA の問題を理解する。
- nested logit を用いて代替性を柔軟に表す。
- 価格が需要ショックと相関する内生性の問題を整理し、操作変数を用いた需要推定を学ぶ。

Reading：

- （主教材）上武ほか『実証ビジネス・エコノミクス』第3章。
- （基礎理論）Berry, Steven T. (1994) "Estimating Discrete-Choice Models of Product Differentiation," *RAND Journal of Economics*, 25(2), 242-262.
- （実証・価格内生性）Villas-Boas, J. Miguel and Russell S. Winer (1999) "Endogeneity in Brand Choice Models," *Management Science*, 45(10), 1324-1338.
- （計量・統計の視点）Berry, Steven T. and Philip A. Haile (2014) "Identification in Differentiated Products Markets Using Market Level Data," *Econometrica*, 82(5), 1749-1797.
- （計量・統計の視点）Gandhi, Amit and Jean-Francois Houde (2019) "Measuring Substitution Patterns in Differentiated-Products Industries," NBER Working Paper No. 26375.

### 第4回　異質性のある需要：random coefficient logit と合併分析

前後とのつながり：第3回の代替性・内生性の問題を踏まえ、消費者異質性を入れた需要推定に拡張する。次回の競争政策ゲスト講義では、推定された代替性や価格反応が実務の合併審査でどう使われるかを見る。

講義内容：

- 消費者ごとに価格感応度や商品属性への好みが異なる状況を扱う。
- random coefficient logit とシミュレーションによる choice probability を学ぶ。
- 個票データ、購買履歴、アンケート情報を用いた micro moments の考え方を紹介する。
- 需要推定から価格弾力性、代替性、合併後の価格変化を評価する merger analysis の考え方につなげる。

Reading：

- （主教材）上武ほか『実証ビジネス・エコノミクス』第4章。
- （実装・需要推定）Nevo, Aviv (2000) "A Practitioner's Guide to Estimation of Random-Coefficients Logit Models of Demand," *Journal of Economics & Management Strategy*, 9(4), 513-548.
- （合併分析）Werden, Gregory J. and Luke M. Froeb (1994) "The Effects of Mergers in Differentiated Products Industries: Logit Demand and Merger Policy," *Journal of Law, Economics, & Organization*, 10(2), 407-426.
- （実証・新製品）Petrin, Amil (2002) "Quantifying the Benefits of New Products: The Case of the Minivan," *Journal of Political Economy*, 110(4), 705-729.
- （計量・統計の視点）Berry, Steven T. and Philip A. Haile (2024) "Nonparametric Identification of Differentiated Products Demand Using Micro Data," *Econometrica*, 92(4), 1135-1162.

### 第5回　ゲスト講義1：競争政策の実務と需要推定

前後とのつながり：第2-4回の需要推定を、競争政策と合併審査の実務に接続する。次回からは、実際の購買データではなく、商品属性を実験的に設計する stated preference の分析へ移る。

講義内容：

- 需要推定、代替性、市場画定、合併審査が競争政策の現場でどのように使われるかを学ぶ。
- 企業結合審査における経済分析の役割を理解する。
- 講義で学んだ需要推定と、実務上の判断との接点を整理する。

Reading：

- （制度資料）公正取引委員会（2004年、2019年改定）「企業結合審査に関する独占禁止法の運用指針」。
- （合併分析・市場画定）Farrell, Joseph and Carl Shapiro (2010) "Antitrust Evaluation of Horizontal Mergers: An Economic Alternative to Market Definition," *The B.E. Journal of Theoretical Economics*, 10(1).
- （合併分析・logit）Werden, Gregory J. and Luke M. Froeb (1994) "The Effects of Mergers in Differentiated Products Industries: Logit Demand and Merger Policy," *Journal of Law, Economics, & Organization*, 10(2), 407-426.
- （合併分析・手法）Jaffe, Sonia and E. Glen Weyl (2013) "The First-Order Approach to Merger Analysis," *American Economic Journal: Microeconomics*, 5(4), 188-218.
- （合併分析・実証）Miller, Nathan H. and Matthew C. Weinberg (2017) "Understanding the Price Effects of the MillerCoors Joint Venture," *Econometrica*, 85(6), 1763-1791.

### 第6回　商品設計とコンジョイント分析：離散選択モデルと多属性ランダム化実験

前後とのつながり：前半の revealed preference による需要推定から、属性をランダム化した stated preference の選択データへ視点を移す。次回のA/Bテストでは、より一般的な施策実験として因果効果を扱う。

講義内容：

- stated preference と revealed preference の違いを整理する。
- 離散選択モデルを、実際の購買データではなく、属性をランダム化した選択データに適用する。
- conjoint analysis / choice-based conjoint を用いて、商品属性、価格、ブランドの価値や支払意思額を推定する。
- コンジョイント分析を多属性のランダム化実験として捉え、AMCE、相互作用、高次元処置の考え方を学ぶ。
- 属性効果の平均と、消費者異質性・セグメンテーションの関係を整理する。

Reading：

- （サーベイ・商品設計）Green, Paul E. and V. Srinivasan (1990) "Conjoint Analysis in Marketing: New Developments with Implications for Research and Practice," *Journal of Marketing*, 54(4), 3-19.
- （教科書・離散選択）Train, Kenneth E. (2009) *Discrete Choice Methods with Simulation*, 2nd ed., Cambridge University Press, Chapter 2.
- （因果推論・AMCE）Hainmueller, Jens, Daniel J. Hopkins, and Teppei Yamamoto (2014) "Causal Inference in Conjoint Analysis: Understanding Multidimensional Choices via Stated Preference Experiments," *Political Analysis*, 22(1), 1-30.
- （因果推論・相互作用）Egami, Naoki and Kosuke Imai (2019) "Causal Interaction in Factorial Experiments: Application to Conjoint Analysis," *Journal of the American Statistical Association*, 114(526), 529-540.
- （計量・統計の視点）Goplerud, Max, Kosuke Imai, and Nicole E. Pashley (2025) "Estimating Heterogeneous Causal Effects of High-Dimensional Treatments: Application to Conjoint Analysis," *Annals of Applied Statistics*, 19(2), 866-888.

### 第7回　マーケティングの因果推論1：実験とA/Bテスト

前後とのつながり：第6回の多属性ランダム化実験を、広告、クーポン、レコメンドなどの施策実験へ広げる。次回は、実験できない場面で観察データから効果を読む方法を扱う。

講義内容：

- 広告、クーポン、レコメンド、メール施策の効果測定を題材に、実験設計を学ぶ。
- incrementality、holdout、intention-to-treat、treatment-on-the-treated を整理する。
- 平均効果と異質的効果の違いを理解する。
- 実験単位、spillover/interference、multiple testing など、大規模実験で生じる実務上の問題に触れる。

Reading：

- （教科書・A/Bテスト）Kohavi, Ron, Diane Tang, and Ya Xu (2020) *Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing*, Cambridge University Press, Chapters 1-3.
- （実証・広告実験）Gordon, Brett R., Florian Zettelmeyer, Neha Bhargava, and Dan Chapsky (2019) "A Comparison of Approaches to Advertising Measurement: Evidence from Big Field Experiments at Facebook," *Marketing Science*, 38(2), 193-225.
- （実証・広告測定）Johnson, Garrett A., Randall A. Lewis, and Elmar I. Nubbemeyer (2017) "Ghost Ads: Improving the Economics of Measuring Online Ad Effectiveness," *Journal of Marketing Research*, 54(6), 867-884.
- （計量・統計の視点）Athey, Susan and Guido W. Imbens (2017) "The Econometrics of Randomized Experiments," in *Handbook of Economic Field Experiments*, Vol. 1, 73-140.


### 第8回　マーケティングの因果推論2：観察データで施策効果を読む

前後とのつながり：第7回の実験をベンチマークに、実験がない状況での識別戦略を学ぶ。次回からは、平均効果だけでなく、消費者ごとの異質性と顧客履歴をどう推定するかに進む。

講義内容：

- 広告接触者と非接触者の単純比較がなぜ効果測定にならないのかを考える。
- difference-in-differences、IV、RDD、panel fixed effects をマーケティング施策に応用する。
- staggered adoption や event study など、近年のDiDで問題になる論点を確認する。
- 価格変更、広告出稿、キャンペーン、ポイント施策における識別の失敗例を扱う。

Reading：

- （レビュー・準実験）Goldfarb, Avi, Catherine E. Tucker, and Yanwen Wang (2022) "Conducting Research in Marketing with Quasi-Experiments," *Journal of Marketing*, 86(3), 1-20.
- （実証・検索広告）Blake, Thomas, Chris Nosko, and Steven Tadelis (2015) "Consumer Heterogeneity and Paid Search Effectiveness: A Large-Scale Field Experiment," *Econometrica*, 83(1), 155-174.
- （実証・広告測定）Lewis, Randall A. and Justin M. Rao (2015) "The Unfavorable Economics of Measuring the Returns to Advertising," *Quarterly Journal of Economics*, 130(4), 1941-1973.
- （計量・統計の視点）Imbens, Guido W. and Jeffrey M. Wooldridge (2009) "Recent Developments in the Econometrics of Program Evaluation," *Journal of Economic Literature*, 47(1), 5-86.
- （計量・統計の視点）Callaway, Brantly and Pedro H. C. Sant'Anna (2021) "Difference-in-Differences with Multiple Time Periods," *Journal of Econometrics*, 225(2), 200-230.

### 第9回　消費者異質性の推定：階層モデルと shrinkage

前後とのつながり：第6-8回で扱った属性効果・施策効果の「平均」から、誰に効くのか、誰がどのように反応するのかという異質性の推定へ進む。次回の顧客パネル分析では、この異質性を購買履歴から推定する。

講義内容：

- 同じ価格、広告、商品属性に対して消費者ごとに反応が異なる状況を定式化する。
- complete pooling、個人別推定、partial pooling の違いを比較する。
- random coefficients、混合分布、階層モデルを、未観測異質性を扱うための道具として理解する。
- 階層ベイズ・経験ベイズにおける shrinkage の直感と、推定不確実性の扱いを学ぶ。
- mixed logit、hierarchical Bayes conjoint、購買履歴モデルが共通して持つ異質性推定の構造を整理する。

Reading：

- （教科書）Rossi, Peter E., Greg M. Allenby, and Robert McCulloch (2005) *Bayesian Statistics and Marketing*, John Wiley & Sons.
- （手法・サーベイ）Allenby, Greg M. and Peter E. Rossi (1999) "Marketing Models of Consumer Heterogeneity," *Journal of Econometrics*, 89(1-2), 57-78.
- （手法・サーベイ）Rossi, Peter E. and Greg M. Allenby (2003) "Bayesian Statistics and Marketing," *Marketing Science*, 22(3), 304-328.
- （手法）Lenk, Peter J., Wayne S. DeSarbo, Paul E. Green, and Martin R. Young (1996) "Hierarchical Bayes Conjoint Analysis: Recovery of Partworth Heterogeneity from Reduced Experimental Designs," *Marketing Science*, 15(2), 173-191.
- （実証）Rossi, Peter E., Robert E. McCulloch, and Greg M. Allenby (1996) "The Value of Purchase History Data in Target Marketing," *Marketing Science*, 15(4), 321-340.

### 第10回　顧客パネルデータのモデル化：購買頻度・離脱・顧客価値予測

前後とのつながり：第9回の階層モデル・shrinkage を、購買履歴や離脱リスクの推定に適用する。次回は、予測された顧客価値や施策効果を使って、誰に何を提示するかというターゲティングの意思決定へ進む。

講義内容：

- 購買履歴データを、個人ごとの購買頻度、購買タイミング、離脱リスクに関する情報として読む。
- 契約型ビジネスと非契約型ビジネスの違いを整理し、離脱が直接観測されない場合の推定問題を理解する。
- Poisson-Gamma、Pareto/NBD、BG/NBD などを例に、購買頻度、離脱、未観測異質性のモデル化を学ぶ。
- 将来購買回数、継続確率、顧客価値を予測し、その不確実性をどう扱うかを考える。
- 顧客価値は予測対象であり、施策配分には因果効果や政策評価が別途必要であることを確認する。

Reading：

- （教科書・レビュー）Fader, Peter S. and Bruce G. S. Hardie (2009) "Probability Models for Customer-Base Analysis," *Journal of Interactive Marketing*, 23(1), 61-69.
- （手法）Schmittlein, David C., Donald G. Morrison, and Richard Colombo (1987) "Counting Your Customers: Who-Are They and What Will They Do Next?" *Management Science*, 33(1), 1-24.
- （手法）Fader, Peter S., Bruce G. S. Hardie, and Ka Lok Lee (2005) "Counting Your Customers the Easy Way: An Alternative to the Pareto/NBD Model," *Marketing Science*, 24(2), 275-284.
- （手法・階層ベイズ）Abe, Makoto (2009) "Counting Your Customers One by One: A Hierarchical Bayes Extension to the Pareto/NBD Model," *Marketing Science*, 28(3), 541-553.
- （実証・モデル比較）Donkers, Bas, Peter C. Verhoef, and Martijn G. de Jong (2007) "Modeling CLV: A Test of Competing Models in the Insurance Industry," *Quantitative Marketing and Economics*, 5(2), 163-190.
- （実証・意思決定）Venkatesan, Rajkumar and V. Kumar (2004) "A Customer Lifetime Value Framework for Customer Selection and Resource Allocation Strategy," *Journal of Marketing*, 68(4), 106-125.

### 第11回　予測から意思決定へ：ターゲティングと離散的施策最適化

前後とのつながり：第9-10回で推定した異質性・顧客価値を、離散的な施策配分に変換する。まず「誰にどの広告・クーポン・レコメンドを出すか」という基本的な意思決定問題を整理する。

講義内容：

- 第9-10回で扱った顧客価値・購買性向の予測と、施策の因果効果を区別する。
- uplift modeling と heterogeneous treatment effects を用いたターゲティングを学ぶ。
- 広告クリエイティブ、クーポン、メール、レコメンドなど、複数の離散的な施策候補から何を割り当てるかを考える。
- 顧客価値の予測と施策の因果効果を組み合わせて、予算制約の下で顧客ごとの施策配分を考える。
- レコメンド、価格、広告配分において、予測モデルをそのまま意思決定に使う危うさを理解する。
- policy learning の考え方を用いて、推定した効果を意思決定ルールに変換する方法を学ぶ。

Reading：

- （実証・警告例）Ascarza, Eva (2018) "Retention Futility: Targeting High-Risk Customers Might Be Ineffective," *Journal of Marketing Research*, 55(1), 80-98.
- （実証・施策評価）Hitsch, Günter J., Sanjog Misra, and Walter W. Zhang (2024) "Heterogeneous Treatment Effects and Optimal Targeting Policy Evaluation," *Quantitative Marketing and Economics*, 22(2), 115-168.
- （手法・機械学習）Athey, Susan and Guido W. Imbens (2019) "Machine Learning Methods That Economists Should Know About," *Annual Review of Economics*, 11, 685-725.
- （手法・異質的効果）Wager, Stefan and Susan Athey (2018) "Estimation and Inference of Heterogeneous Treatment Effects Using Random Forests," *Journal of the American Statistical Association*, 113(523), 1228-1242.
- （手法・政策学習）Kitagawa, Toru and Aleksey Tetenov (2018) "Who Should Be Treated? Empirical Welfare Maximization Methods for Treatment Choice," *Econometrica*, 86(2), 591-616.
- （手法・DML）Chernozhukov, Victor, Denis Chetverikov, Mert Demirer, Esther Duflo, Christian Hansen, Whitney Newey, and James Robins (2018) "Double/Debiased Machine Learning for Treatment and Structural Parameters," *The Econometrics Journal*, 21(1), C1-C68.

### 第12回　ゲスト講義2：エコノミストによる実務講義

前後とのつながり：第6-11回で扱った実験、因果推論、異質性、ターゲティングが、企業内の意思決定でどう使われるかを確認する。

講義内容：

- 大規模実験、需要予測、価格、広告、レコメンド、マーケットプレイス分析など、Big techのエコノミストが扱う問いを学ぶ。
- 研究としての経済学と、事業意思決定としての経済学の違いを理解する。
- データ、実験、モデル、組織内コミュニケーションの関係を考える。

Reading：

- （実務・技術企業）Athey, Susan and Michael Luca (2019) "Economists (and Economics) in Tech Companies," *Journal of Economic Perspectives*, 33(1), 209-230.
- （実務・ビッグデータ）Einav, Liran and Jonathan Levin (2014) "Economics in the Age of Big Data," *Science*, 346(6210), 1243089.
- （ゲスト指定資料）ゲスト講師が指定する資料。

### 第13回　動学的離散選択1：RustとHotz-Miller

前後とのつながり：第10-12回で扱った購買履歴・潜在状態・実務上の意思決定を、forward-looking な逐次的意思決定へ拡張する。次回は、この基礎をロイヤルティ、価格差別、買いだめ、セールの応用に接続する。

講義内容：

- 状態変数、状態遷移、価値関数、Bellman equation、choice-specific value function の考え方を学ぶ。
- Rust のバスエンジン交換モデルを通じて、動学的構造モデルが何を識別し、どのような反実仮想を可能にするかを理解する。
- Hotz-Miller の conditional choice probability approach を用いて、選択確率から価値関数の差を復元する考え方を学ぶ。
- 静学的な需要推定や顧客価値予測に対して、forward-looking behavior を仮定することの利点とコストを整理する。

Reading：

- （基礎理論）Rust, John (1987) "Optimal Replacement of GMC Bus Engines: An Empirical Model of Harold Zurcher," *Econometrica*, 55(5), 999-1033.
- （基礎理論）Hotz, V. Joseph and Robert A. Miller (1993) "Conditional Choice Probabilities and the Estimation of Dynamic Models," *Review of Economic Studies*, 60(3), 497-529.
- （手法・サーベイ）Aguirregabiria, Victor and Pedro Mira (2010) "Dynamic Discrete Choice Structural Models: A Survey," *Journal of Econometrics*, 156(1), 38-67.
- （実装・サーベイ）Arcidiacono, Peter and Paul B. Ellickson (2011) "Practical Methods for Estimation of Dynamic Discrete Choice Models," *Annual Review of Economics*, 3, 363-394.

### 第14回　動学的離散選択2：スイッチングコスト、ロイヤルティ、買いだめ

前後とのつながり：第13回で学んだ forward-looking な消費者モデルを、ロイヤルティ、スイッチングコスト、在庫、セールへの反応に応用する。第15回では、企業側の動学的な価格設定問題へ進む。

講義内容：

- ロイヤルティ、学習、スイッチングコスト、在庫、参照価格を、動学的な状態変数として捉える。
- state dependence と未観測の消費者異質性をどのように区別するかを考える。
- 一時的値下げ、セール、プロモーションが将来需要を前借りする場合、静学的な需要推定が何を見誤るかを理解する。
- 買いだめや価格期待があるとき、短期価格弾力性と長期価格弾力性がなぜ異なるかを学ぶ。
- 最も単純な価格差別として、観測可能なタイプや履歴に応じて異なる価格・割引を提示する考え方を確認する。
- 動学的モデルを用いた価格政策、販促政策、ロイヤルティ施策の反実仮想分析に触れる。

Reading：

- （価格差別・基礎）Varian, Hal R. (1989) "Price Discrimination," in *Handbook of Industrial Organization*, Vol. 1, 597-654.
- （動学的ブランド選択）Erdem, Tulin and Michael P. Keane (1996) "Decision-Making Under Uncertainty: Capturing Dynamic Brand Choice Processes in Turbulent Consumer Goods Markets," *Marketing Science*, 15(1), 1-20.
- （価格不確実性・数量選択）Erdem, Tulin, Susumu Imai, and Michael P. Keane (2003) "Brand and Quantity Choice Dynamics Under Price Uncertainty," *Quantitative Marketing and Economics*, 1(1), 5-64.
- （買いだめ・セール）Hendel, Igal and Aviv Nevo (2006) "Measuring the Implications of Sales and Consumer Inventory Behavior," *Econometrica*, 74(6), 1637-1673.
- （状態依存・慣性）Dube, Jean-Pierre, Günter J. Hitsch, and Peter E. Rossi (2010) "State Dependence and Alternative Explanations for Consumer Inertia," *RAND Journal of Economics*, 41(3), 417-445.
- （学習モデル・サーベイ）Ching, Andrew T., Tulin Erdem, and Michael P. Keane (2013) "Learning Models: An Assessment of Progress, Challenges, and New Developments," *Marketing Science*, 32(6), 913-938.

### 第15回　Dynamic pricing：企業の動学的価格設定

前後とのつながり：第13-14回では消費者側の動学的な選択を扱った。第15回では視点を企業側に移し、時間、需要状態、容量、在庫に応じて価格を変える dynamic pricing を扱う。

講義内容：

- dynamic pricing における「dynamic」を、企業の価格ルールが状態や時間に応じて変わることとして整理する。
- 価格を連続的な意思決定変数として扱い、需要弾力性、容量制約、時間変動する需要、在庫の機会費用を整理する。
- peak-load pricing と real-time pricing を、時間帯や需給状態に応じた価格設定として理解する。
- 航空券やホテルなど、販売期限と容量制約がある市場における dynamic pricing / revenue management の基本モデルを学ぶ。
- ride-hailing の surge pricing を、需要と供給の不均衡、待ち時間、マッチング摩擦を調整する価格として理解する。
- 価格最適化を実装する際に、需要推定、因果効果、顧客異質性、企業の動学的最適化がどのように結びつくかを総括する。

Reading：

- （peak-load pricing）Steiner, Peter O. (1957) "Peak Loads and Efficient Pricing," *Quarterly Journal of Economics*, 71(4), 585-610.
- （real-time pricing）Borenstein, Severin (2005) "The Long-Run Efficiency of Real-Time Electricity Pricing," *The Energy Journal*, 26(3), 93-116.
- （在庫制約・基礎理論）Gallego, Guillermo and Garrett van Ryzin (1994) "Optimal Dynamic Pricing of Inventories with Stochastic Demand over Finite Horizons," *Management Science*, 40(8), 999-1020.
- （surge pricing・基礎理論）Galichon, Alfred and Yu-Wei Hsieh (2017) "A Theory of Decentralized Matching Markets without Transfers, with an Application to Surge Pricing," USC-INET Research Paper No. 17-03.
- （航空券・実証）Williams, Kevin R. (2022) "The Welfare Effects of Dynamic Pricing: Evidence from Airline Markets," *Econometrica*, 90(2), 831-858.

## 成績評価

- Coding課題：40%
  - 講義内容に対応するデータ分析課題を4回課す。各課題では、需要推定、コンジョイント分析、実験・因果推論、消費者異質性・顧客分析、ターゲティング・価格最適化などに関する簡単な実装と結果の解釈を行う。
- 査読レポート：30%
  - Reading listに含まれる文献から2本を選び、それぞれについて査読レポートを作成する。研究の問い、識別戦略・モデル、データ、貢献、限界、改善案を簡潔に整理する。
- 期末レポート：30%
  - Research proposalを提出する。講義で扱った手法のいずれかを用いて、価格、広告、商品設計、顧客分析、ターゲティング、競争政策に関する実証研究の問いを設定し、必要なデータ、識別戦略またはモデル、予想される貢献を整理する。
