---
license: gemma
datasets:
- agentlans/personal-information-prompts
base_model:
- intfloat/multilingual-e5-small
pipeline_tag: text-classification
tags:
- pii
- multilingual
- privacy
- redaction
---
# Gemma 3 Embedding 300M PII Detector

A lightweight multilingual model for detecting personally identifiable information (PII) in text.

It achieves the following results on the evaluation set:

- Loss: 0.2924
- Accuracy: 0.8978
- Input tokens seen during training: 4&thinsp;552&thinsp;704  

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    task="text-classification",
    model="agentlans/embeddinggemma-300m-pii-detector"
)

classifier("Your text here.")
# [{'label': 'False', 'score': 0.9987590312957764}]
```

## Results

<details>
  <summary>Translated testing text</summary>

**English**
1. My full name is John Michael Doe, and I reside at 123 Elm Street, Springfield, IL 62701.
2. Contact me at my email address: john.doe@email.com or by phone at (555) 123-4567.
3. My Social Security Number is 123-45-6789, which I use for official identifications.
4. I was born on June 15, 1985, in the city of Chicago, Illinois.
5. My driver's license number is DL-987654321, issued by the state of Illinois.
6. Please send packages to my home address: 456 Oak Avenue, Apartment 2B, New York, NY 10001.
7. My passport number is PP-1122334455, valid until December 31, 2030.
8. For banking, use my account number 9876543210 at First National Bank.
9. My credit card details include the number 4111-1111-1111-1111 with expiration 12/28.
10. I work at Tech Corp, employee ID 56789, located at 789 Pine Road, Austin, TX 78701.
11. My full name is [NAME REDACTED], and I live on [STREET NAME] in a medium-sized city.
12. You can reach the project team using the shared contact form on our internal portal.
13. For identity verification in this demo, the system displays a mock identification code like XXX-XX-XXXX instead of a real number.
14. The example user profile shows a fictional birth date field paired with a generic city of birth label.
15. A sample record might include a placeholder license field labeled “LICENSE-#########” to mimic real-world formats without using actual data.
16. The test shipping label uses “Sample Recipient” and “Example Street” to illustrate how addresses are structured.
17. In the training dashboard, a dummy travel document number is shown only as a sequence of repeating characters.
18. The banking screen includes a fake account identifier such as “ACCOUNT-0000000000” to emulate a real account layout.
19. A mock payment card entry uses a pattern like “1111-2222-3333-4444” that does not correspond to an actual card.
20. The HR sample record lists “Test Employee” with a generic office location field to demonstrate employee data formatting.

**French**
1. Je m'appelle John Michael Doe et je réside au 123, rue Elm, Springfield, Illinois 62701.
2. Vous pouvez me contacter par courriel à l'adresse john.doe@email.com ou par téléphone au (555) 123-4567.
3. Mon numéro de sécurité sociale est le 123-45-6789 ; je l'utilise pour mes pièces d'identité officielles.
4. Je suis né le 15 juin 1985 à Chicago, dans l'Illinois.
5. Mon numéro de permis de conduire est le DL-987654321 ; il a été délivré par l'État de l'Illinois.
6. Veuillez envoyer les colis à mon domicile : 456 Oak Avenue, Appartement 2B, New York, NY 10001.
7. Mon numéro de passeport est PP-1122334455 et il est valide jusqu’au 31 décembre 2030.
8. Pour vos opérations bancaires, veuillez utiliser mon numéro de compte 9876543210 à la First National Bank.
9. Les informations relatives à ma carte de crédit sont les suivantes : numéro 4111-1111-1111-1111 et date d’expiration : 28/12.
10. Je travaille chez Tech Corp, sous le numéro d’employé 56789, au 789 Pine Road, Austin, TX 78701.
11. Mon nom complet est [NOM MASQUÉ] et j’habite au [NOM DE LA RUE] dans une ville de taille moyenne.
12. Vous pouvez contacter l’équipe projet via le formulaire de contact partagé sur notre portail interne.
13. Pour la vérification d'identité dans cette démonstration, le système affiche un code d'identification fictif, par exemple XXX-XX-XXXX, au lieu d'un numéro réel.
14. Le profil utilisateur d'exemple présente un champ de date de naissance fictif associé à une ville de naissance générique.
15. Un enregistrement d'exemple peut inclure un champ de permis de conduire factice intitulé « PERMIS-########## » afin de simuler des formats réels sans utiliser de données réelles.
16. L'étiquette d'expédition de test utilise « Destinataire fictif » et « Rue fictive » pour illustrer la structure des adresses.
17. Dans le tableau de bord de formation, un numéro de document de voyage fictif est affiché uniquement sous forme de séquence de caractères répétitifs.
18. L'écran bancaire inclut un identifiant de compte fictif, tel que « COMPTE-0000000000 », afin d'imiter la structure d'un compte réel.
19. Une saisie de carte de paiement fictive utilise un format comme « 1111-2222-3333-4444 » qui ne correspond à aucune carte réelle.
20. L'exemple d'enregistrement RH mentionne « Employé test » avec un champ générique de localisation de bureau pour illustrer le formatage des données des employés.

**Spanish**
1. Mi nombre completo es John Michael Doe y resido en 123 Elm Street, Springfield, IL 62701.
2. Puede contactarme por correo electrónico: john.doe@email.com o por teléfono al (555) 123-4567.
3. Mi número de Seguro Social es 123-45-6789, el cual utilizo para identificaciones oficiales.
4. Nací el 15 de junio de 1985 en la ciudad de Chicago, Illinois.
5. Mi número de licencia de conducir es DL-987654321, emitido por el estado de Illinois.
6. Por favor, envíen los paquetes a mi domicilio: 456 Oak Avenue, Apartamento 2B, Nueva York, NY 10001.
7. Mi número de pasaporte es PP-1122334455, válido hasta el 31 de diciembre de 2030.
8. Para operaciones bancarias, utilice mi número de cuenta 9876543210 en First National Bank.
9. Los datos de mi tarjeta de crédito incluyen el número 4111-1111-1111-1111, con vencimiento el 28/12.
10. Trabajo en Tech Corp, con ID de empleado 56789, ubicado en 789 Pine Road, Austin, TX 78701.
11. Mi nombre completo es [NOMBRE OMITIDO] y vivo en [NOMBRE DE LA CALLE] en una ciudad mediana.
12. Puede contactar con el equipo del proyecto mediante el formulario de contacto compartido en nuestro portal interno.
13. Para la verificación de identidad en esta demostración, el sistema muestra un código de identificación ficticio como XXX-XX-XXXX en lugar de un número real.
14. El perfil de usuario de ejemplo muestra un campo de fecha de nacimiento ficticio junto con una etiqueta genérica de ciudad de nacimiento.
15. Un registro de ejemplo podría incluir un campo de licencia de marcador de posición denominado "LICENCIA-#########" para imitar formatos reales sin usar datos reales.
16. La etiqueta de envío de prueba utiliza "Destinatario de muestra" y "Calle de ejemplo" para ilustrar la estructura de las direcciones.
17. En el panel de entrenamiento, un número de documento de viaje ficticio se muestra únicamente como una secuencia de caracteres repetidos.
18. La pantalla bancaria incluye un identificador de cuenta falso como "CUENTA-0000000000" para emular el diseño de una cuenta real.
19. Una entrada de tarjeta de pago simulada utiliza un patrón como "1111-2222-3333-4444", que no corresponde a una tarjeta real.
20. El registro de muestra de RR.HH. incluye “Empleado de prueba” con un campo de ubicación de oficina genérico para demostrar el formato de los datos de los empleados.

**Chinese**
1. 我的全名是约翰·迈克尔·多伊 (John Michael Doe)，居住在伊利诺伊州斯普林菲尔德市榆树街123号 (123 Elm Street, Springfield, IL 62701)。
2. 您可以通过邮箱 john.doe@email.com 或电话 (555) 123-4567 联系我。
3. 我的社会安全号码是 123-45-6789，我用它来办理官方身份证明。
4. 我于1985年6月15日出生于伊利诺伊州芝加哥市。
5. 我的驾照号码是 DL-987654321，由伊利诺伊州颁发。
6. 请将包裹寄送到我的家庭住址：纽约州纽约市橡树大道456号2B公寓，邮编10001。
7. 我的护照号码是PP-1122334455，有效期至2030年12月31日。
8. 我的银行账户是First National Bank，账号为9876543210。
9. 我的信用卡卡号为4111-1111-1111-1111，有效期至12月28日。
10. 我在Tech Corp工作，员工编号为56789，公司地址为德克萨斯州奥斯汀市松树路789号，邮编78701。
11. 我的全名是[姓名已编辑]，居住在[街道名称]，位于一座中等规模的城市。
12. 您可以通过我们内部门户网站上的共享联系表格联系项目团队。
13. 在本演示中，为进行身份验证，系统会显示类似 XXX-XX-XXXX 的模拟识别码，而非真实号码。
14. 示例用户个人资料中包含一个虚构的出生日期字段，并搭配一个通用的出生城市标签。
15. 示例记录可能包含一个占位符许可证字段，标签为“LICENSE-#########”，以模拟真实世界的格式，而无需使用实际数据。
16. 测试发货标签使用“示例收件人”和“示例街道”来演示地址的结构。
17. 在培训仪表板中，虚拟旅行证件号码仅显示为一串重复字符。
18. 银行界面包含一个类似“ACCOUNT-0000000000”的虚假账户标识符，以模拟真实账户布局。
19. 模拟支付卡条目使用类似“1111-2222-3333-4444”的模式，该模式与实际的支付卡不符。
20. 人力资源示例记录列出了“测试员工”，其中包含一个通用的办公地点字段，用于演示员工数据格式。

**Russian**
1. Моё полное имя — Джон Майкл Доу, я проживаю по адресу: Элм-стрит, 123, Спрингфилд, Иллинойс, 62701.
2. Свяжитесь со мной по электронной почте: john.doe@email.com или по телефону: (555) 123-4567.
3. Мой номер социального страхования — 123-45-6789, который я использую для официальных удостоверений личности.
4. Я родился 15 июня 1985 года в городе Чикаго, штат Иллинойс.
5. Номер моего водительского удостоверения — DL-987654321, выдано штатом Иллинойс.
6. Пожалуйста, отправляйте посылки на мой домашний адрес: 456 Oak Avenue, Apartment 2B, New York, NY 10001.
7. Номер моего паспорта: PP-1122334455, действителен до 31 декабря 2030 года.
8. Для банковских операций используйте мой счёт 9876543210 в First National Bank.
9. В данных моей кредитной карты указан номер 4111-1111-1111-1111, срок действия — 28 декабря.
10. Я работаю в компании Tech Corp, идентификационный номер сотрудника: 56789, адрес: 789 Pine Road, Austin, TX 78701.
11. Моё полное имя: [ИМЯ УДАЛЕНО], я живу на [НАЗВАНИЕ УЛИЦЫ] в городе среднего размера.
12. Вы можете связаться с командой проекта, используя общую контактную форму на нашем внутреннем портале.
13. Для подтверждения личности в этой демонстрации система отображает фиктивный идентификационный код, например XXX-XX-XXXX, вместо реального числа.
14. В примере профиля пользователя показано поле вымышленной даты рождения в сочетании с общей меткой города рождения.
15. В примере записи может быть использовано поле лицензии-заглушка с меткой «LICENSE-#########», имитирующее реальные форматы без использования реальных данных.
16. В тестовой этикетке для доставки используются поля «Sample Recipient» и «Example Street» для иллюстрации структуры адресов.
17. На учебной панели управления фиктивный номер проездного документа отображается только в виде последовательности повторяющихся символов.
18. На экране банковских операций отображается фиктивный идентификатор счёта, например, «ACCOUNT-0000000000», для имитации макета реального счёта.
19. В записи фиктивной платёжной карты используется шаблон типа «1111-2222-3333-4444», который не соответствует реальной карте.
20. В образце записи отдела кадров указан «Тестовый сотрудник» с общим полем местоположения офиса для демонстрации форматирования данных о сотруднике.

**Arabic**
1. اسمي الكامل جون مايكل دو، وأقيم في ١٢٣ شارع إلم، سبرينغفيلد، إلينوي ٦٢٧٠١.
2. للتواصل معي عبر بريدي الإلكتروني: john.doe@email.com أو عبر الهاتف على الرقم (٥٥٥) ١٢٣-٤٥٦٧.
3. رقم الضمان الاجتماعي الخاص بي هو ١٢٣-٤٥-٦٧٨٩، وهو رقم أستخدمه لإثبات هويتي الرسمية.
4. وُلدتُ في ١٥ يونيو ١٩٨٥ في مدينة شيكاغو، إلينوي.
5. رقم رخصة قيادتي هو DL-٩٨٧٦٥٤٣٢١، صادرة عن ولاية إلينوي.
6. يرجى إرسال الطرود إلى عنوان منزلي: 456 شارع أوك، شقة 2ب، نيويورك، نيويورك 10001.
7. رقم جواز سفري هو PP-1122334455، صالح حتى 31 ديسمبر 2030.
8. للمعاملات المصرفية، استخدم رقم حسابي 9876543210 في بنك فيرست ناشيونال.
9. تتضمن بيانات بطاقتي الائتمانية الرقم 4111-1111-1111-1111، وتاريخ انتهاء الصلاحية 28/12.
10. أعمل في شركة Tech Corp، رقم تعريف الموظف 56789، الكائنة في 789 طريق باين، أوستن، تكساس 78701.
11. اسمي الكامل هو [تم حذف الاسم]، وأعيش في [اسم الشارع] في مدينة متوسطة الحجم.
12. يمكنك التواصل مع فريق المشروع باستخدام نموذج الاتصال المشترك على بوابتنا الداخلية.
13. للتحقق من الهوية في هذا العرض التوضيحي، يعرض النظام رمز تعريف وهمي مثل XXX-XX-XXXX بدلاً من رقم حقيقي.
14. يعرض ملف تعريف المستخدم النموذجي حقل تاريخ ميلاد وهمي مقترنًا بعلامة مدينة ميلاد عامة.
15. قد يتضمن سجل نموذجي حقل ترخيص بديل بعنوان "LICENSE-#########" لمحاكاة التنسيقات الحقيقية دون استخدام بيانات فعلية.
16. يستخدم ملصق الشحن التجريبي "نموذج المستلم" و"مثال الشارع" لتوضيح كيفية هيكلة العناوين.
17. في لوحة معلومات التدريب، يظهر رقم وثيقة سفر وهمي فقط كتسلسل من الأحرف المتكررة.
18. تتضمن شاشة الخدمات المصرفية معرف حساب وهمي مثل "ACCOUNT-0000000000" لمحاكاة تخطيط حساب حقيقي.
19. يستخدم إدخال بطاقة دفع وهمي نمطًا مثل "1111-2222-3333-4444" لا يتوافق مع بطاقة فعلية.
20. تسرد سجلات الموارد البشرية النموذجية "موظف الاختبار" مع حقل موقع مكتب عام لإظهار تنسيق بيانات الموظف.
</details>

<details>
<summary>Testing results</summary>

Classification results for identical texts translated into different languages

- 🚫 means that the model detected PII in the input
- ◯ means that the model detected no PII in the input
  
|English sentence|English|French|Spanish|Chinese|Russian|Arabic|
|---|:---:|:---:|:---:|:---:|:---:|:---:|
|My full name is John Michael Doe, and I reside at 123 Elm Street, Springfield, IL 62701.|🚫|🚫|🚫|🚫|🚫|◯|
|Contact me at my email address: john.doe@email.com or by phone at (555) 123-4567.|🚫|🚫|🚫|🚫|🚫|🚫|
|My Social Security Number is 123-45-6789, which I use for official identifications.|🚫|🚫|🚫|🚫|🚫|🚫|
|I was born on June 15, 1985, in the city of Chicago, Illinois.|🚫|🚫|🚫|◯|🚫|◯|
|My driver's license number is DL-987654321, issued by the state of Illinois.|🚫|◯|🚫|🚫|🚫|◯|
|Please send packages to my home address: 456 Oak Avenue, Apartment 2B, New York, NY 10001.|🚫|🚫|🚫|◯|🚫|🚫|
|My passport number is PP-1122334455, valid until December 31, 2030.|🚫|◯|🚫|🚫|🚫|🚫|
|For banking, use my account number 9876543210 at First National Bank.|🚫|🚫|🚫|🚫|🚫|🚫|
|My credit card details include the number 4111-1111-1111-1111 with expiration 12/28.|🚫|🚫|🚫|🚫|🚫|🚫|
|I work at Tech Corp, employee ID 56789, located at 789 Pine Road, Austin, TX 78701.|🚫|🚫|🚫|🚫|🚫|🚫|
|My full name is [NAME REDACTED], and I live on [STREET NAME] in a medium-sized city.|◯|◯|◯|◯|◯|◯|
|You can reach the project team using the shared contact form on our internal portal.|◯|🚫|◯|🚫|🚫|◯|
|For identity verification in this demo, the system displays a mock identification code like XXX-XX-XXXX instead of a real number.|🚫|🚫|◯|◯|◯|🚫|
|The example user profile shows a fictional birth date field paired with a generic city of birth label.|◯|◯|◯|◯|◯|◯|
|A sample record might include a placeholder license field labeled “LICENSE-#########” to mimic real-world formats without using actual data.|◯|◯|◯|◯|◯|◯|
|The test shipping label uses “Sample Recipient” and “Example Street” to illustrate how addresses are structured.|◯|◯|◯|◯|◯|◯|
|In the training dashboard, a dummy travel document number is shown only as a sequence of repeating characters.|◯|◯|◯|◯|◯|◯|
|The banking screen includes a fake account identifier such as “ACCOUNT-0000000000” to emulate a real account layout.|◯|◯|◯|🚫|🚫|◯|
|A mock payment card entry uses a pattern like “1111-2222-3333-4444” that does not correspond to an actual card.|◯|◯|◯|◯|◯|◯|
|The HR sample record lists “Test Employee” with a generic office location field to demonstrate employee data formatting.|◯|◯|◯|◯|◯|◯|

</details>

## Limitations

- False positives on some inputs (for example, certain number patterns or locale-specific identifiers).  
- May perform poorly on very short texts that lack sufficient context.  
- Not a drop-in replacement for legal or compliance review; should be used as an assistive tool.

## Training

### Hyperparameters

- learning_rate: 5e-05  
- train_batch_size: 8  
- eval_batch_size: 8  
- seed: 42  
- optimizer: `AdamW` (fused) with `betas=(0.9, 0.999)`, `eps=1e-08`, no additional optimizer arguments  
- lr_scheduler_type: linear  
- num_epochs: 3.0  

### Framework versions

- Transformers 5.0.0.dev0  
- PyTorch 2.9.1+cu128  
- Datasets 4.4.1  
- Tokenizers 0.22.1  

## Licence

Gemma terms of service

## See also

[agentlans/multilingual-e5-small-pii-detector](https://huggingface.co/agentlans/multilingual-e5-small-pii-detector) has fewer false positives but is less sensitive.
