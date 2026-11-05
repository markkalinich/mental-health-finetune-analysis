---
license: cc-by-sa-4.0
datasets:
- procesaur/ZNANJE
- procesaur/STARS
- procesaur/Vikipedija
- jerteh/SrpELTeC
- procesaur/kisobran
language:
- sr
- hr
base_model:
- FacebookAI/xlm-roberta-large
---

<table style="width:100%;height:100%">
  <tr>
<td colspan=2>
  <h4><i class="highlight-container"><b class="highlight">TeslaXLM</b></i></h4>
</td>
    </tr>
  <tr style="width:100%;height:100%">
    <td width=50%>
      <p>Вишејезични модел, 561 милион параметара</p>
      <p>Обучаван над корпусима српског и српскохрватског језика - 20 милијарди речи</p>
      <p>Једнака подршка уноса на ћирилици и латиници!</p>
    </td>
    <td>
      <p>Multilingual model, 561 million parameters</p>
      <p>Trained on Serbian and Serbo-Croatian corpora - 20 billion words</p>
      <p>Equal support for Cyrillic and Latin input!</p>
    </td>
  </tr>
  </table>

```python
>>> from transformers import pipeline
>>> unmasker = pipeline('fill-mask', model='te-sla/teslaXLM')
>>> unmasker("Kada bi čovek znao gde će pasti on bi<mask>.")
```

```python
>>> from transformers import AutoTokenizer, AutoModelForMaskedLM
>>> from torch import LongTensor, no_grad
>>> from scipy import spatial
>>> tokenizer = AutoTokenizer.from_pretrained('te-sla/teslaXLM')
>>> model = AutoModelForMaskedLM.from_pretrained('te-sla/teslaXLM', output_hidden_states=True)
>>> x = " pas"
>>> y = " mačka"
>>> z = " svemir"
>>> tensor_x = LongTensor(tokenizer.encode(x, add_special_tokens=False)).unsqueeze(0)
>>> tensor_y = LongTensor(tokenizer.encode(y, add_special_tokens=False)).unsqueeze(0)
>>> tensor_z = LongTensor(tokenizer.encode(z, add_special_tokens=False)).unsqueeze(0)
>>> model.eval()
>>> with no_grad():
>>>     vektor_x = model(input_ids=tensor_x).hidden_states[-1].squeeze()
>>>     vektor_y = model(input_ids=tensor_y).hidden_states[-1].squeeze()
>>>     vektor_z = model(input_ids=tensor_z).hidden_states[-1].squeeze()
>>>     print(spatial.distance.cosine(vektor_x, vektor_y))
>>>     print(spatial.distance.cosine(vektor_x, vektor_z))
```

<table style="width:100%;height:100%">
<tr>
<td width=50%>
  <h5><i class="highlight-container"><b class="highlight">Евалуација XLMR модела за српски језик</b></i></h4>
</td>
<td>
  <h5><i class="highlight-container"><b class="highlight">Serbian XLMR models evaluation results</b></i></h4>
</td>
</tr>
  <tr colspan=2 style="width:100%;height:100%">
    <td colspan=2 >
    <img src="xlm-fm.png" class="cover" style="max-width:650px">
      <img src="xlm-pr.png" class="cover" style="max-width:650px">
      <img src="xlm-ds.png" class="cover" style="max-width:650px">
    </td>
  </tr>
  </table>

<div class="inline-flex flex-col avatar-cont">
  <div class="avatar-title">Author</div>
    <a href="https://huggingface.co/procesaur">  
      <div class="flex">
          <div class="avatar-cover"
  			style="background-image: url(&#39;https://cdn-uploads.huggingface.co/production/uploads/1673534533167-63bc254fb8c61b8aa496a39b.jpeg?w=200&h=200&f=face&#39;)">
          </div>
      </div>
      <div class="avatar-name">Mihailo Škorić</div>
      <div class="avatar-handle">@procesaur</div>
    </a>
  </div>
</div>

<div class="inline-flex flex-col avatar-cont">
  <div class="avatar-title">Editor</div>
    <a href="https://huggingface.co/tanor">  
      <div class="flex">
          <div class="avatar-cover"
  			style="background-image: url(https://cdn-avatars.huggingface.co/v1/production/uploads/6409d3d71ee054d66a673701/KTOOnCRS9NhpAMZIvLlU7.png?w=200&h=200&f=face)">
          </div>
      </div>
      <div class="avatar-name">Saša Petalinkar</div>
      <div class="avatar-handle">@tanor</div>
    </a>
  </div>
</div>

<div class="inline-flex flex-col avatar-cont">
  <div class="avatar-title">Computation</div>
    <a href="https://tesla.rgf.bg.ac.rs">  
      <div class="flex">
          <div class="avatar-cover"
  			style="background-image: url(https://cdn-avatars.huggingface.co/v1/production/uploads/63bc254fb8c61b8aa496a39b/TfM_-sc8-b34ddfhHBGTA.png?w=200&h=200&f=face)">
          </div>
      </div>
      <div class="avatar-name">TESLA project</div>
      <div class="avatar-handle">@te-sla</div>
    </a>
  </div>
</div>


<div class="inline-flex flex-col avatar-cont">
  <div class="avatar-title">Funding</div>
    <a href="https://fondzanauku.gov.rs/">  
      <div class="flex">
          <div class="avatar-cover"
  			style="background-image: url(https://fondzanauku.gov.rs/wp-content/uploads/2019/04/FZN-logo-primary-light-1170x396.png)">
          </div>
      </div>
      <div class="avatar-name">Fond za Nauku</div>
      <div class="avatar-handle">@fondzanauku_rs</div>
    </a>
  </div>
</div>

## Cit.

```bibtex
@incollection{skoric2025:juznoslovenskijezici,
  author       = {Škorić, Mihailo and Petalinkar, Saša},
  orcid        = {0000-0003-4811-8692 and 0009-0007-9664-3594},
  title        = {Quality Textual Corpora and New South Slavic Language Models},
  license      = {https://creativecommons.org/licenses/by/4.0/},
  booktitle    = {Proceedings of the International Conference South Slavic Languages in the Digital Environment JuDig : Thematic Collection of Papers},
  editor       = {Moskovljević Popović, Jasmina and Stanković, Ranka},
  isbn         = {978-86-6153-791-2},
  series       = {South Slavic Languages in the Digital Environment JuDig},
  publisher    = {University of Belgrade — Faculty of Philology},
  address      = {Belgrade},
  year         = {2025},
  volume       = {1},
  pages        = {337--348},
  note         = {19},
  doi          = {10.18485/judig.2025.1.ch19},
  doiurl       = {http://doi.fil.bg.ac.rs/volume.php?pt=eb_ser&issue=judig-2025-1&i=19},
  url          = {http://doi.fil.bg.ac.rs/pdf/eb_ser/judig/2025-1/judig-2025-1-ch19.pdf}
}
```

<br/>

<div id="zastava">
  <div class="grb">
    <img src="https://www.ai.gov.rs/img/logo_60x120-2.png" style="position:relative; left:30px; z-index:10; height:85px">
  </div>
  <table width=100% style="border:0px">
    <tr style="background-color:#C6363C;width:100%;border:0px;height:30px"><td style="width:100vw"></td></tr>
    <tr style="background-color:#0C4076;width:100%;border:0px;height:30px"><td></td></tr>
    <tr style="background-color:#ffffff;width:100%;border:0px;height:30px"><td></td></tr>
  </table>
</div>

<table style="width:100%;height:100%">
  <tr style="width:100%;height:100%">
    <td width=50%>
       <p>Истраживање jе спроведено уз подршку Фонда за науку Републике Србиjе, #7276, Text Embeddings – Serbian Language Applications – TESLA</p>
    </td>
    <td>
      <p>This research was supported by the Science Fund of the Republic of Serbia, #7276, Text Embeddings - Serbian Language Applications - TESLA</p>
    </td>
  </tr>
</table>



<style>
  .ffeat: {
  color:red
  }
  
  .cover {
    width: 100%;
    margin-bottom: 5pt
  }
  
.highlight-container, .highlight {
  position: relative;
  text-decoration:none
}

.highlight-container {
  display: inline-block;
}

.avatar-cont {
  line-height: 1.5;
  padding-right:50px;
}

.avatar-title{
  text-align: center;
  margin-top: 3px;
  font-size: 16px;
  font-weight: 800;
}

.avatar-name{
  text-align: center;
  font-size: 16px;
  font-weight: 800;
}

.avatar-handle{
  text-align: center;
  font-size: 14px;
}

.avatar-cover{
  display:DISPLAY_1;
  margin-left: auto;
  margin-right: auto;
  width: 92px;
  height:92px;
  border-radius: 50%;
  background-position: center;
  background-size: contain;
  background-repeat: no-repeat;
}

.highlight{
  color:white;
  text-transform:uppercase;
  font-size: 16pt;
}

  .highlight-container{
    padding:5px 10px
  }

.highlight-container:before {
  content: " ";
  display: block;
  height: 100%;
  width: 100%;
  margin-left: 0px;
  margin-right: 0px;
  position: absolute;
  background: #e80909;
  transform: rotate(2deg);
  top: -1px;
  left: -1px;
  border-radius: 20% 25% 20% 24%;
  padding: 10px 18px 18px 10px;
}

div.grb, #zastava>table {
  position:absolute;
  top:0px;
  left: 0px;
  margin:0px
}

  div.grb>img, #zastava>table{
    margin:0px
  }
  
#zastava {
  position: relative;
  margin-bottom:120px
}

  p {
    font-size:14pt
  }
</style>