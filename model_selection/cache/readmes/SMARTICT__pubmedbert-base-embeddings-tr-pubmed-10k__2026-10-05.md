---
language:
- tr
license: apache-2.0
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:10001
- loss:MultipleNegativesRankingLoss
base_model: NeuML/pubmedbert-base-embeddings
widget:
- source_sentence: İran'ın İsfahan şehrinde bir Bakır-T (Cu-T) IUD yerleştirme programında
    eğitilmiş ebe kadınların değerlendirilmesi. İsfahan’daki dört merkezden, ebe kadınlar
    tarafından yapılan 252 Cu-T-200 yerleştirmesi ve doktorlar tarafından yapılan
    646 yerleştirme verileri karşılaştırılmıştır. Ebe tarafından yerleştirilen kadınlar
    için net birikimli bir yıl devam etme oranı, doktor tarafından yerleştirilen kadınlara
    göre anlamlı derecede daha düşük olmasına rağmen, iki hasta grubunun ilk yıl olay
    oranları arasında önemli bir fark bulunmamaktadır. Bu veriler, ebe kadınların
    IUD yerleştirme programlarındaki rolünün genişletilmesinin sağlık personelinin
    etkin kullanımı olacağını önermektedir.
  sentences:
  - İsfahan’daki dört merkezde gerçekleştirilen Cu-T-200 yerleştirmeleriyle ilgili
    veriler nasıl karşılaştırılmıştır?
  - Pankreatin bileşiğinin lipaz aktivitesi üzerine yapılan çalışmaların temel amacı
    nedir?
  - Benzodiazepin esterlerinin farmakokinetik çalışmalarında kullanılan gaz-sıvı kromatografisi
    yöntemi hangi ilacı ve metabolitlerini tespit etmek için geliştirilmiştir?
- source_sentence: Memelilerin mitokondriyanın iç zarındaki protein kinaz aktivitesi.
    Bu makale, memelilerin mitokondriyanın iç zarına bağlı bir protein kinaz aktivitesinin
    keşfi hakkında bilgi vermektedir. Enzim, siklik AMP veya siklik GMP eklenmesine
    yanıt vermez ve fosfat kabul edicisi olarak bütün histone tercih eder. Siklik
    nükleotid bağımlı sitozol protein kinazlarına ait bazı standart test sistemleri,
    orthofosfat konsantrasyonu 25 mM'den yüksek ve test pH'ı 6.5'in altındaysa bu
    aktiviteyi tespit edemeyebilir. Burada tanımlanan enzim, görünürde pH optimumu
    8.5’dir. Karaciğer mitokondrilerinde aktivite, mitokondriler ya sonikasyon ya
    da dondurma ve çözme işlemleriyle bozulmadıkça belirgin değildir. Hem karaciğer
    hem de kalp mitokondri soniketlerinin merkezkaç fraksiyonlarındaki kinaz aktivitesi,
    succinat dehydrogenase ve sitokrom oksidaz gibi iç zar belirteç enzimleriyle paralel
    olarak dağılım gösterirken, sitoplazma enzimleri olan malik dehidrogenazdan oldukça
    farklıdır. Dış ve iç zar ile zenginleştirilmiş preparatlarla yapılan deneyler,
    bu enzimlerin iç zar üzerinde yer aldığını doğrulamıştır. Çünkü iç zarın, dış
    zarın fosfatta şişirilerek bozulmasından sonra ortaya çıkan dondurma ve çözme
    işleminden sonra tam aktivite gösterimi için gerekli olduğu görüldü, bu da geçici
    olarak sonucuna varılmıştır ki, substrate sadece iç zarın matriks tarafından kabul
    edilir.
  sentences:
  - Metinde tanımlanan enzimlerin aktifliği hangi pH aralığında en yüksek seviyededir
    ve enzim aktivitesi hakkında ne söylenmiştir?
  - Amfoterisin B'nin (AMB) kaplumbağa mesanesindeki hidrojen iyonu ve bikarbonat
    iyonu geçirgenliği üzerindeki etkisi nedir?
  - Düşük ve yüksek pH ortamlarının fare interferonunun stabilitesi üzerindeki etkileri
    nedir?
- source_sentence: 'İnsanlarda β-adrenerjik stimülasyonun antidüretik etkisinin mekanizması.
    Hayvanlarda isoproterenol hidroklorür ile yapılan β-adrenerjik stimülasyon, antidiüretik
    hormonla benzer bir antidürezis oluşturur. Bu araştırma, isoproterenol''un insanlarda
    su diyuresini engelleyip engellemediğini belirlemek amacıyla yapıldı. Yedi genç
    erkek gönüllü, üç aşamada su diyuresi sırasında incelendi: (1) su yükleme, (2)
    su yükleme plus isoproterenol, ve (3) su yükleme plus isoproterenol plus propranolol
    hidroklorür. Antidürezis, isoproterenol infüzyonu sonrası 20 dakika içinde meydana
    geldi ve bu süre zarfında diyare hızı ortalama 19,4 ml/dakikadan 2,0 ml/dakikaya
    düştü (0,03 mikrog ila 0,06 mikrog/kg/dak). Bulgularımız, antidürezisin hormonel
    (antidiüretik hormon) ve hormonel olmayan değişikliklere (glomerüler filtrasyon
    hızında ve renal plazma akışında azalma) bağlı olduğunu gösterdi. Bunlar da sırasıyla
    ilacın kardiyovasküler etkilerinden kaynaklanmaktadır.'
  sentences:
  - İskemik anoksiyanın domuz mide elektriksel ve mekanik aktivite üzerinde etkisi
    nasıl gözlemlenmiştir?
  - Jamaikalı kadınların servikslerinde en sık bulunan morfolojik özellik nedir ve
    bu özellik hangi bölge üzerinde yoğunlaşmıştır?
  - İnsanlarda β-adrenerjik stimülasyonun antidüretik etkisinin mekanizması nedir?
- source_sentence: 'Sarcoma 180 hücreleri ile sıçan karaciğerinde adenozin fosforilaz
    ve inosine-guanosine fosforilaz aktivitelerinden farklı olarak, adenozin fosforilaz
    (EC 2.4.2.-) aktivitesinin kültürde üretilen Sarcoma 180 hücreleri ve sıçan karaciğerinde
    bulunduğu ve birkaç kriterle inosine-guanosine fosforilaz aktivitesinden farklı
    olduğu gösterilmiştir: (a) Sarcoma 180 hücre özütü p-kloromerküri benzoat ile
    muamele edildiğinde, iki aktivite farklı derecede inhibe olmuştur. (b) Adenin,
    Sarcoma 180 ve sıçan karaciğer özütlerinin adenozin fosforilaz aktivitesini ısı
    inaktivasyonuna karşı seçici olarak korurken, hypoxanthin inosine-guanosine fosforilaz
    aktivitesini seçici olarak korumuştur. (c) Neredeyse doygun substrat konsantrasyonlarında
    ve Sarcoma 180 özütü kullanılarak, adenine + hypoxanthine veya adenine + guanine
    karışımlarının ribozilasyon hızları, hypoxanthine + guanine karışımına kıyasla,
    ayrı ayrı ölçülen hızların toplamına yaklaşık olarak eşit bulunmuştur. (d) inosine,
    Sarcoma 180 ve sıçan karaciğer özütleri tarafından katalize edilen hypoxanthine
    ve guanine ribozilasyonunu seçici biçimde engellerken, 2-kloroadenozin adenine
    ve N6-furfuriladenine ribozilasyonunu seçici biçimde engellemiştir. (e) pH-aktivite
    eğrileri, hypoxanthine veya guanine substrat olarak kullanıldığında benzer iken,
    adenine ile yapılan eğri belirgin şekilde farklıdır. Adenozin fosforilaz aktivitesinin
    in vivo''daki potansiyel rolü tartışılmıştır.'
  sentences:
  - Sarcoma 180 hücreleri ve sıçan karaciğerinde adenozin fosforilaz ile inosine-guanosine
    fosforilaz aktiviteleri arasında hangi farklar gösterilmiştir?
  - Metinde bahsedilen gruplar kimlerden oluşmaktadır?
  - Köpek serumundaki monoamin oksidazın (MAO) optimum pH değeri nedir ve bu değer
    tavşan serumundaki MAO'nunkinden nasıl farklıdır?
- source_sentence: 'Kuşlarda saldırganlık-ilişkili davranışlar. II. AA gen ürünlerinin
    hücresel ekspresyonu. B1-anti-B2 ve B2-anti-B1 allosera, sırasıyla, homozygot
    B1/1 ve B2/2 tavukların damar içi aşısı yoluyla, aşağıdaki kaynaklardan elde edilen
    B1/2 hücreleriyle immunizasyon sağlanarak üretildi: periferik kan lökositleri
    (PBL), eritrositler, timus hücreleri ve bursa hücreleri. Bu alloseralardan saflaştırılmış
    süspansiyonlar, hem kırmızı kan hücrelerini hem de orijinal verici türünün kan
    lenfositlerinin GVH reaktivitesini güçlü biçimde inhibe eden anti-B alloserumu
    antikorları üretti. Aynı dört kaynaktan hücreler kullanılarak yapılan sera emilim
    çalışmaları, bu antikorların GVH inhibisyonunu sağlayan antikorları tamamen uzaklaştırabildiğini
    gösterdi. Özellikle önemli bir gerçek, eritrositler ve lenfositlerde ortak olan
    B-haplotype belirlenmiş antijenlerin, daha önce tanımlandığı gibi (Simonsen 1975),
    allo-saldırganlık loci gen ürünlerini içeriyor olabileceğidir.'
  sentences:
  - B1-anti-B2 ve B2-anti-B1 alloseralardan elde edilen antikorların üretiminde hangi
    hücre kaynakları kullanılmıştır?
  - Orta miyokardiyal ve subendokardiyal pH’nin izlenmesi hangi amaçla kullanılmıştır?
  - Metinde incelenen hormon ile yağ hücrelerindeki adenilat siklaz sistemi arasındaki
    etkileşimin amacı nedir?
datasets:
- SMARTICT/pubmed_tr_10k
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- cosine_accuracy@1
- cosine_accuracy@3
- cosine_accuracy@5
- cosine_accuracy@10
- cosine_precision@1
- cosine_precision@3
- cosine_precision@5
- cosine_precision@10
- cosine_recall@1
- cosine_recall@3
- cosine_recall@5
- cosine_recall@10
- cosine_ndcg@10
- cosine_mrr@10
- cosine_map@100
model-index:
- name: pubmedbert-base-embeddings
  results:
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: dim 768
      type: dim_768
    metrics:
    - type: cosine_accuracy@1
      value: 0.8143712574850299
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.8782435129740519
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.9021956087824351
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.9281437125748503
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.8143712574850299
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.29274783765801726
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.18043912175648705
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.09281437125748504
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.8143712574850299
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.8782435129740519
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.9021956087824351
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.9281437125748503
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.8712526863238155
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.8531349998415868
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.8547375639294634
      name: Cosine Map@100
---

# pubmedbert-base-embeddings

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [NeuML/pubmedbert-base-embeddings](https://huggingface.co/NeuML/pubmedbert-base-embeddings) on the [pubmed_tr_10k](https://huggingface.co/datasets/SMARTICT/pubmed_tr_10k) dataset. It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [NeuML/pubmedbert-base-embeddings](https://huggingface.co/NeuML/pubmedbert-base-embeddings) <!-- at revision d6eaca8254bc229f3ca42749a5510ae287eb3486 -->
- **Maximum Sequence Length:** 512 tokens
- **Output Dimensionality:** 768 dimensions
- **Similarity Function:** Cosine Similarity
- **Training Dataset:**
    - [pubmed_tr_10k](https://huggingface.co/datasets/SMARTICT/pubmed_tr_10k)
- **Language:** tr
- **License:** apache-2.0

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/UKPLab/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': False}) with Transformer model: BertModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    'Kuşlarda saldırganlık-ilişkili davranışlar. II. AA gen ürünlerinin hücresel ekspresyonu. B1-anti-B2 ve B2-anti-B1 allosera, sırasıyla, homozygot B1/1 ve B2/2 tavukların damar içi aşısı yoluyla, aşağıdaki kaynaklardan elde edilen B1/2 hücreleriyle immunizasyon sağlanarak üretildi: periferik kan lökositleri (PBL), eritrositler, timus hücreleri ve bursa hücreleri. Bu alloseralardan saflaştırılmış süspansiyonlar, hem kırmızı kan hücrelerini hem de orijinal verici türünün kan lenfositlerinin GVH reaktivitesini güçlü biçimde inhibe eden anti-B alloserumu antikorları üretti. Aynı dört kaynaktan hücreler kullanılarak yapılan sera emilim çalışmaları, bu antikorların GVH inhibisyonunu sağlayan antikorları tamamen uzaklaştırabildiğini gösterdi. Özellikle önemli bir gerçek, eritrositler ve lenfositlerde ortak olan B-haplotype belirlenmiş antijenlerin, daha önce tanımlandığı gibi (Simonsen 1975), allo-saldırganlık loci gen ürünlerini içeriyor olabileceğidir.',
    'B1-anti-B2 ve B2-anti-B1 alloseralardan elde edilen antikorların üretiminde hangi hücre kaynakları kullanılmıştır?',
    'Metinde incelenen hormon ile yağ hücrelerindeki adenilat siklaz sistemi arasındaki etkileşimin amacı nedir?',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 768]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities.shape)
# [3, 3]
```

<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

## Evaluation

### Metrics

#### Information Retrieval

* Dataset: `dim_768`
* Evaluated with [<code>InformationRetrievalEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.InformationRetrievalEvaluator) with these parameters:
  ```json
  {
      "truncate_dim": 768
  }
  ```

| Metric              | Value      |
|:--------------------|:-----------|
| cosine_accuracy@1   | 0.8144     |
| cosine_accuracy@3   | 0.8782     |
| cosine_accuracy@5   | 0.9022     |
| cosine_accuracy@10  | 0.9281     |
| cosine_precision@1  | 0.8144     |
| cosine_precision@3  | 0.2927     |
| cosine_precision@5  | 0.1804     |
| cosine_precision@10 | 0.0928     |
| cosine_recall@1     | 0.8144     |
| cosine_recall@3     | 0.8782     |
| cosine_recall@5     | 0.9022     |
| cosine_recall@10    | 0.9281     |
| **cosine_ndcg@10**  | **0.8713** |
| cosine_mrr@10       | 0.8531     |
| cosine_map@100      | 0.8547     |

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### pubmed_tr_10k

* Dataset: [pubmed_tr_10k](https://huggingface.co/datasets/SMARTICT/pubmed_tr_10k) at [7c6016f](https://huggingface.co/datasets/SMARTICT/pubmed_tr_10k/tree/7c6016f2a0b4289a597f8273e8a333802f6deae3)
* Size: 10,001 training samples
* Columns: <code>positive</code> and <code>anchor</code>
* Approximate statistics based on the first 1000 samples:
  |         | positive                                                                            | anchor                                                                             |
  |:--------|:------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
  | type    | string                                                                              | string                                                                             |
  | details | <ul><li>min: 43 tokens</li><li>mean: 401.5 tokens</li><li>max: 512 tokens</li></ul> | <ul><li>min: 15 tokens</li><li>mean: 44.33 tokens</li><li>max: 91 tokens</li></ul> |
* Samples:
  | positive                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | anchor                                                                                                                                    |
  |:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>Bakteriyofaj P22'nin baz plaket parçalarının enzimik ve moleküler özellikleri. Substrat olarak 14C ile işaretlenmiş Salmonella bakteriyel hücreleri kullanılarak, P22 firkası baz plaket parçalarının enzimik ve moleküler özellikleri incelendi. Baz plaket parçası, Salmonella typhimurium, Salmonella schottmuellerie ve Salmonella typhi’nin O-antijenini kapsamlı şekilde kesen tek bir protein türünden oluşuyordu; ayrıcalıklı olarak Salmonella typhimurium ve Salmonella schottmuellerie’nin O-antijenini, Salmonella typhi’den biraz daha yavaş bir hızda kesiyor ve indirgenmiş uçta rhamnose bulunan oligoşaride ürünler salıyordu. P22’ya lizogenik olan bir Salmonella typhimurium suşunda ise çok daha az kesme gerçekleşti ve Salmonella anatum, Salmonella newington ve Salmonella minneapolis üzerinde ise anlamlı bir reaksiyon gözlenmedi. Baz plaket parçası enzim, çok ısıya dayanıklı bir protein olup, 85 derece C’de 5 dakika boyunca muamele sonrası sadece %10-20 kayıp gözlemlendi. Enzimin pH optimali yakl...</code> | <code>P22 baz plaket parçasının enzimik özellikleri nelerdir ve hangi substratları keser?</code>                                          |
  | <code>Fare T ve B lenfositlerinin nakil karşıtı reaksiyona katılımı. CBA farelerinin dalak veya lenf nodu hücreleri, kısmi dozda ışınlanmış (CBAXC57BL/6)F1 farelerine nakledildi; bu, nakil karşıtı reaksiyonun (GVHR) gelişmesine neden oldu. Lenfositler, fare T ve B lenfositlerine karşı spesifik serumlar ile in vitro muamele edildikten sonra bu reaksiyonu gerçekleştirme yeteneklerini kaybetti. Görünüşe göre, farelerde GVHR'nin gelişimi, T ve B lenfositlerinin işbirlikçi etkileşimiyle bağlantılıydı.</code>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | <code>Farelerde nakil karşıtı reaksiyonun (GVHR) gelişmesi hangi hücrelerin katılımıyla ilişkilidir?</code>                               |
  | <code>2,3-diphosphoglycerat'in insan kanındaki tamponlama özellikleri üzerindeki etkisi: kırmızı kan hücresi zarının rolü. İnsan kanının tamponlama özellikleri ve hücre dışı ile hücre içi pH (deltapHi/deltapHe) arasındaki ilişkinin eğimi (eğimi) üzerindeki 2,3-diphosphoglycerat (2,3-DPG, 0.5-21 mikromol/g hücre) konsantrasyonunun etkisi incelendi. Sonuçlar, 2,3-DPG'nin Donnan oranı rH+ = H+e/H+i üzerindeki etkisiyle ilgili önceki bulgularla bağlantılı olarak değerlendirildi. deltapHi/deltapHe değeri, kırmızı kan hücresindeki 2,3-DPG miktarının artmasıyla ve ekstrasellüler pH'nın yükselmesiyle azalmaktadır. deltapHi/deltapHe ile rH+ birbirine aşağıdaki ampirik denklemle bağlanabilir: deltapHi/deltapHe = 1 + log rH+ = 1 + pHi - pHe. Bu denklemin geçerliliği, Donnan oranı rH+'nin 0.3 ile 1 arasında değiştiği koşullarla sınırlı görünmektedir; bu değişiklikler ya 2,3-DPG gibi tamponlayıcı anyonların kırmızı kan hücrelerindeki konsantrasyonundaki değişiklikler ya da ekzosellüler pH'daki değişiklik...</code> | <code>2,3-diphosphoglycerat (2,3-DPG) konsantrasyonunun artması kırmızı kan hücresinde deltapHi/deltapHe değerine nasıl etki eder?</code> |
* Loss: [<code>MultipleNegativesRankingLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#multiplenegativesrankingloss) with these parameters:
  ```json
  {
      "scale": 20.0,
      "similarity_fct": "cos_sim"
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `eval_strategy`: epoch
- `per_device_train_batch_size`: 32
- `per_device_eval_batch_size`: 16
- `gradient_accumulation_steps`: 16
- `learning_rate`: 2e-05
- `num_train_epochs`: 5
- `lr_scheduler_type`: cosine
- `warmup_ratio`: 0.1
- `bf16`: True
- `tf32`: True
- `load_best_model_at_end`: True
- `optim`: adamw_torch_fused
- `batch_sampler`: no_duplicates

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: epoch
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 32
- `per_device_eval_batch_size`: 16
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 16
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 2e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1.0
- `num_train_epochs`: 5
- `max_steps`: -1
- `lr_scheduler_type`: cosine
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.1
- `warmup_steps`: 0
- `log_level`: passive
- `log_level_replica`: warning
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `save_safetensors`: True
- `save_on_each_node`: False
- `save_only_model`: False
- `restore_callback_states_from_checkpoint`: False
- `no_cuda`: False
- `use_cpu`: False
- `use_mps_device`: False
- `seed`: 42
- `data_seed`: None
- `jit_mode_eval`: False
- `use_ipex`: False
- `bf16`: True
- `fp16`: False
- `fp16_opt_level`: O1
- `half_precision_backend`: auto
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: True
- `local_rank`: 0
- `ddp_backend`: None
- `tpu_num_cores`: None
- `tpu_metrics_debug`: False
- `debug`: []
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_prefetch_factor`: None
- `past_index`: -1
- `disable_tqdm`: False
- `remove_unused_columns`: True
- `label_names`: None
- `load_best_model_at_end`: True
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_min_num_params`: 0
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `fsdp_transformer_layer_cls_to_wrap`: None
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `deepspeed`: None
- `label_smoothing_factor`: 0.0
- `optim`: adamw_torch_fused
- `optim_args`: None
- `adafactor`: False
- `group_by_length`: False
- `length_column_name`: length
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `skip_memory_metrics`: True
- `use_legacy_prediction_loop`: False
- `push_to_hub`: False
- `resume_from_checkpoint`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_private_repo`: None
- `hub_always_push`: False
- `hub_revision`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `include_inputs_for_metrics`: False
- `include_for_metrics`: []
- `eval_do_concat_batches`: True
- `fp16_backend`: auto
- `push_to_hub_model_id`: None
- `push_to_hub_organization`: None
- `mp_parameters`: 
- `auto_find_batch_size`: False
- `full_determinism`: False
- `torchdynamo`: None
- `ray_scope`: last
- `ddp_timeout`: 1800
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `include_tokens_per_second`: False
- `include_num_input_tokens_seen`: False
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `eval_use_gather_object`: False
- `average_tokens_across_devices`: False
- `prompts`: None
- `batch_sampler`: no_duplicates
- `multi_dataset_batch_sampler`: proportional

</details>

### Training Logs
| Epoch   | Step    | Training Loss | dim_768_cosine_ndcg@10 |
|:-------:|:-------:|:-------------:|:----------------------:|
| 0.5112  | 10      | 1.2023        | -                      |
| 1.0     | 20      | 0.2711        | 0.8182                 |
| 1.5112  | 30      | 0.1766        | -                      |
| 2.0     | 40      | 0.1464        | 0.8500                 |
| 2.5112  | 50      | 0.1112        | -                      |
| 3.0     | 60      | 0.0984        | 0.8614                 |
| 3.5112  | 70      | 0.087         | -                      |
| 4.0     | 80      | 0.0791        | 0.8691                 |
| 4.5112  | 90      | 0.0811        | -                      |
| **5.0** | **100** | **0.0726**    | **0.8713**             |

* The bold row denotes the saved checkpoint.

### Framework Versions
- Python: 3.11.13
- Sentence Transformers: 4.1.0
- Transformers: 4.53.1
- PyTorch: 2.6.0+cu124
- Accelerate: 1.8.1
- Datasets: 4.0.0
- Tokenizers: 0.21.2

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

#### MultipleNegativesRankingLoss
```bibtex
@misc{henderson2017efficient,
    title={Efficient Natural Language Response Suggestion for Smart Reply},
    author={Matthew Henderson and Rami Al-Rfou and Brian Strope and Yun-hsuan Sung and Laszlo Lukacs and Ruiqi Guo and Sanjiv Kumar and Balint Miklos and Ray Kurzweil},
    year={2017},
    eprint={1705.00652},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->