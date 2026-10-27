# ASBMB Education Feature Archive

A backup of the articles published in the **ASBMB Education Feature** of the *Australian Biochemist*, the magazine of the Australian Society for Biochemistry and Molecular Biology (ASBMB). It covers 54 articles from 17 issues, from Vol 52 No 1 (April 2021) to Vol 57 No 2 (August 2026).

Each article is stored twice. There is a Markdown copy that GitHub displays directly, and a web page built from the ASBMB website's Education page template.

## Repository layout

```
asbmb-education-feature-archive/
├── README.md                      ← this index
├── templates/
│   ├── asbmb-education-page.html  ← the website Education page the article pages are based on
│   └── asbmb-education-feature-page.html  ← the website Australian Biochemist Education Feature page
├── website/
│   └── education-page-article-links.html  ← link list to paste into the Education Feature page
├── site/
│   └── build.py                   ← builds the GitHub Pages copy of the website pages (see below)
├── .github/workflows/pages.yml    ← publishes that copy to GitHub Pages
└── <year>/
    └── vol-<volume>-no-<number>-<month>/
        ├── README.md              ← issue contents
        └── <article-slug>/
            ├── README.md          ← article (Markdown, renders on GitHub)
            ├── education-feature-<article-slug>.html  ← article (website page)
            └── images/            ← figures (figure-1.jpg …) and author photos (author-<name>.jpg)
```

## Issues

### [April 2021 – Vol 52 No 1](2021/vol-52-no-1-april/README.md)

- [A Picture Paints a Thousand Words: Infographics for Authentic Learning in Undergraduate Students](2021/vol-52-no-1-april/a-picture-paints-a-thousand-words/README.md) – Saw Hoon Lim and Rosa McCarty
- [The Journey from Teaching Face-to-face, to Online, and Back Again – Revealing Four Important Elements of Effective Teaching and Learning](2021/vol-52-no-1-april/face-to-face-to-online-and-back-again/README.md) – Nikki Curthoys
- [Silver Linings of Rapidly Transformed Biochemistry Laboratory Teaching During the COVID-19 Pandemic](2021/vol-52-no-1-april/silver-linings-of-rapidly-transformed-biochemistry-laboratory-teaching/README.md) – Joanne Castelli, Sean Ramsey, Alyssa Van Dreumel and Peter Arthur
- [Skill Development in the Online Laboratory Class](2021/vol-52-no-1-april/skill-development-in-the-online-laboratory-class/README.md) – Jessica Gibbons

### [August 2021 – Vol 52 No 2](2021/vol-52-no-2-august/README.md)

- [Designing Learning Opportunities to Enrich Student Understanding Through Community and Professional Engagement](2021/vol-52-no-2-august/designing-learning-opportunities-through-community-engagement/README.md) – Lois Balmer
- [Planting the Seeds of Learning in the Future Biochemist](2021/vol-52-no-2-august/planting-the-seeds-of-learning-in-the-future-biochemist/README.md) – Melissa Pitman
- [Zooming in on Seven Recommendations for Online Teaching](2021/vol-52-no-2-august/zooming-in-on-seven-recommendations-for-online-teaching/README.md) – Emma Gamble, Jessica Gibbons and Nirma Samarawickrema

### [December 2021 – Vol 52 No 3](2021/vol-52-no-3-december/README.md)

- [Student Panel: Perspectives on Assessment and Academic Integrity at the 2021 ASBMB Education Symposium](2021/vol-52-no-3-december/student-panel-assessment-and-academic-integrity/README.md) – Tracey Kuit (University of Wollongong) and Amber Willems-Jones (University of Melbourne) talk to undergraduate Biochemistry students Taku Chitambo, Eleanor Lawton-Wade and Ella Scott.

### [April 2022 – Vol 53 No 1](2022/vol-53-no-1-april/README.md)

- [Avoid a Collision with Collusion: an Academic Integrity Module Embedded in a First-year Cell Biology Subject](2022/vol-53-no-1-april/avoid-a-collision-with-collusion/README.md) – Ann Parkinson¹, Eva Hatje¹,², Mary Kynn³ and Nicole Reinke¹
- [On the Fly: a Rubric Balancing the Need for Speed and Provision of Feedback – the Oral Presentation](2022/vol-53-no-1-april/on-the-fly-rubric-for-oral-presentations/README.md) – Alyssa Van Dreumel and Peter Arthur
- [Student and Staff Perspectives on Online Proctored and Open-book Exams](2022/vol-53-no-1-april/student-and-staff-perspectives-on-online-proctored-exams/README.md) – Matthew Clemson and Alice Huang

### [August 2022 – Vol 53 No 2](2022/vol-53-no-2-august/README.md)

- [Tutorial Presentation Redesign to Improve Engagement and Development of Core Skills](2022/vol-53-no-2-august/tutorial-presentation-redesign-to-improve-engagement-and-development/README.md) – Jody Gorman
- [Shifts in Student Behaviours During COVID-19: Impacts of Social Interaction on Academic Integrity](2022/vol-53-no-2-august/shifts-in-student-behaviours-during-covid-19/README.md) – Ann Rogerson
- [Using Digital Technologies to Create an Engaging Small Group Learning Experience in Large Cohorts](2022/vol-53-no-2-august/digital-technologies-for-small-group-learning-in-large-cohorts/README.md) – Michelle Rank

### [December 2022 – Vol 53 No 3](2022/vol-53-no-3-december/README.md)

- [The Student Perspective: Advice from Students on What Teaching Academics Should Take With Them From the Pandemic](2022/vol-53-no-3-december/the-student-perspective-advice-from-students/README.md) – Amber Willems-Jones (University of Melbourne) and Tracey Kuit (University of Wollongong) talk to undergraduate Biochemistry students Ishika Jaitly, Marcus Go, Darlene Sentosa and Janelle Accheni.
- [Trafficking the Interdisciplinary Mindset Beyond the Intracurricular Space](2022/vol-53-no-3-december/trafficking-the-interdisciplinary-mindset-beyond-the-intracurricular-space/README.md) – Saw Hoon Lim, Jiangli Tan and Ger Post

### [April 2023 – Vol 54 No 1](2023/vol-54-no-1-april/README.md)

- [Development of a Metacognitive Mindset to Improve Student Learning in Biochemistry](2023/vol-54-no-1-april/metacognitive-mindset-to-improve-student-learning/README.md) – Kathryn Jones
- [Refreshing a Biochemistry Curriculum: A Pinch of Problem-Based Learning, a Dash of Peer-Mentoring, Blended Together with Online Interactive Modules](2023/vol-54-no-1-april/refreshing-a-biochemistry-curriculum/README.md) – James Tsatsaronis, Katrina Binger, Julian Pakay, Lakshmi Wijeyewickrema, Fiona Durand, Fiona Carroll and Noni Frankenberg
- [Student Partners: Strengthening Staff–Student Connections Beyond the Pandemic](2023/vol-54-no-1-april/student-partners-strengthening-staff-student-connections/README.md) – Anne Galea, Kristin Turnbull and Collins Fleischner

### [August 2023 – Vol 54 No 2](2023/vol-54-no-2-august/README.md)

- [Inclusive Laboratory Practice: Perspectives of a Second-year Undergraduate Student](2023/vol-54-no-2-august/inclusive-laboratory-practice/README.md) – Amber Willems-Jones and Alexander Rey (University of Melbourne) talk to undergraduate Biochemistry student Michael Blyth
- [ChemBraille: 3D Chemical Models for the Vision Impaired](2023/vol-54-no-2-august/chembraille-3d-chemical-models-for-the-vision-impaired/README.md) – Aaron Oakley
- [Open-book and Open-AI Mindset: Strategies to Redesign Final Exams in Response to Generative AI and the Potential for Academic Misconduct](2023/vol-54-no-2-august/open-book-and-open-ai-mindset/README.md) – Eduardo Araujo Oliveira and Sarah Frankland

### [December 2023 – Vol 54 No 3](2023/vol-54-no-3-december/README.md)

- [Empowering Students Through Curriculum Choices and Assessment Design: A Students as Partners Approach That Enhances Engagement and Assessment Literacy](2023/vol-54-no-3-december/empowering-students-through-curriculum-choices-and-assessment-design/README.md) – Chris Love
- [Getting the ‘VIBE’ in Biochemistry Education (Virtual Reality In Biochemistry Education)](2023/vol-54-no-3-december/getting-the-vibe-in-biochemistry-education-virtual-reality/README.md) – Anna Lohningᵃ, Susan Hallᵇ, Oladayo Folasireᵃ, Ryan Wirthᵃ and Shai Anoopkumar-Dukieᵇ
- [Assessment Workload – It’s Not About the Number](2023/vol-54-no-3-december/assessment-workload-its-not-about-the-number/README.md) – Fiona Carroll

### [April 2024 – Vol 55 No 1](2024/vol-55-no-1-april/README.md)

- [Laboratory Data Generators: Extending the Teaching Lab Online with Real Results](2024/vol-55-no-1-april/laboratory-data-generators/README.md) – Matthew Clemson, Alice Huang and Gareth Denyer
- [Learning by Design: Combining Experiment and Data Generation for Senior Undergraduate Biochemistry Student Research Projects](2024/vol-55-no-1-april/learning-by-design/README.md) – Jacqueline Matthews and Gareth Denyer
- [Using an Assessment Literacy Module to Improve Scientific Report Writing](2024/vol-55-no-1-april/assessment-literacy-module-to-improve-scientific-report-writing/README.md) – Amber Willems-Jones
- [Cells at War: A Game-based Approach to Learning Biochemistry](2024/vol-55-no-1-april/cells-at-war/README.md) – Reece Sophocleous¹, Danielle Warren¹, Jean-Paul Amore², Rosa Da Silva³ and Tracey Kuit¹
- [IUBMB–FAOBMB Education Symposium at the 30th FAOBMB Conference](2024/vol-55-no-1-april/iubmb-faobmb-education-symposium-30th-faobmb-conference/README.md) – Nirma Samarawickrema

### [August 2024 – Vol 55 No 2](2024/vol-55-no-2-august/README.md)

- [Educator and Student Reflections on Supervising and Conducting Biochemistry Education-based Research](2024/vol-55-no-2-august/reflections-on-supervising-biochemistry-education-research/README.md) – Jordan Witchard and James Tsatsaronis
- [Premeditated Blunders to Trigger Cognitive Learning in Biochemistry: Perceptions of Undergraduate and Postgraduate Students Pursuing Medical Sciences](2024/vol-55-no-2-august/premeditated-blunders-to-trigger-cognitive-learning-in-biochemistry/README.md) – Sheethal Mohan¹, Chandrika Nayak² and Ullas Kamath²
- [Fixing the Kinks in the COIL of Work Integrated Learning](2024/vol-55-no-2-august/fixing-the-kinks-in-the-coil-of-work-integrated-learning/README.md) – Jessica Borger¹,²,³, Megan Taylor¹,² and Kyoko Hombo⁴

### [December 2024 – Vol 55 No 3](2024/vol-55-no-3-december/README.md)

- [Building Career-ready Scientists: Developing Transferable Skills in Science Education](2024/vol-55-no-3-december/building-career-ready-scientists/README.md) – Jane AL Kouba and Tracey Kuit
- [Key Considerations for Effectively Engaging Students With Hands-on Learning Activities](2024/vol-55-no-3-december/engaging-students-with-hands-on-learning-activities/README.md) – Christian Moro and Charlotte Phelps
- [Designing Open Education Resources: the Importance of the Third Space](2024/vol-55-no-3-december/designing-open-education-resources/README.md) – Julian Pakay¹ and Steven Chang²

### [April 2025 – Vol 56 No 1](2025/vol-56-no-1-april/README.md)

- [Two Lanes Forward: the Concept of Trust and the University of Sydney’s Response to Generative AI and Assessment](2025/vol-56-no-1-april/two-lanes-forward/README.md) – Matthew Clemson
- [The Challenges Students Experience When Applying Quantitative Literacy Skills in a Practical Biochemistry Context](2025/vol-56-no-1-april/the-challenges-students-experience-when-applying-quantitative-literacy/README.md) – Amber Willems-Jones¹, Thi Thu Giang Tran² and Jan van Driel²
- [Crossing the Pacific: an Academic’s Experience of Transnational Education](2025/vol-56-no-1-april/crossing-the-pacific/README.md) – Alyssa Van Dreumel

### [August 2025 – Vol 56 No 2](2025/vol-56-no-2-august/README.md)

- [Getting to the CoRe of Flow Cytometry: a New Teaching Framework](2025/vol-56-no-2-august/getting-to-the-core-of-flow-cytometry/README.md) – Jessica Borger¹ and Andrew Filby²
- [Preparing the Next Generation of Students for AI-Driven Biomedical Research: Opportunities in Higher Education](2025/vol-56-no-2-august/preparing-students-for-ai-driven-biomedical-research/README.md) – Joshua Hardy, Dylan Silke, Ashley Weir, Daniel Brown, Kerry Ko, Brendan Ansell, Jessica Borger and Megan Taylor
- [Education Activities at the 31st FAOBMB Conference in Busan, Korea](2025/vol-56-no-2-august/education-activities-at-the-31st-faobmb-conference/README.md) – Tracey Kuit

### [December 2025 – Vol 56 No 3](2025/vol-56-no-3-december/README.md)

- [The Australian Core Concepts of Biochemistry & Molecular Biology](2025/vol-56-no-3-december/australian-core-concepts-of-biochemistry-and-molecular-biology/README.md) – Amber Willems-Jones
- [Reflecting on the Journey: Combining Biology and Chemistry for Health Science Students in the Foundation Year](2025/vol-56-no-3-december/reflecting-on-the-journey/README.md) – Juliana Antonipillai
- [Enhancing Career Confidence and Employability With a New Approach to Career Development and Work-Integrated Learning in Undergraduate Science Degrees](2025/vol-56-no-3-december/enhancing-career-confidence-and-employability/README.md) – Sharon La Fontaine¹,², Cathy Caballero³, Jen Chung², Sharon Berman², Julius Daguman Jr¹, Lynda O’Sullivan¹,⁴, Amanda McPherson¹, Karen Young⁴ and Anthony R. Rendall¹
- [Navigating the AI Landscape: Insights from Australian Biochemistry Educators](2025/vol-56-no-3-december/navigating-the-ai-landscape/README.md) – Matthew Clemson

### [April 2026 – Vol 57 No 1](2026/vol-57-no-1-april/README.md)

- [Lessons Learnt From Interactive Oral Assessments at Scale in a First-year Molecular Biology Unit](2026/vol-57-no-1-april/lessons-learnt-from-interactive-oral-assessments-at-scale/README.md) – Masha Smallhorn and Narelle Hunter
- [Science Fiction Prototyping: Making the Impossible, Possible](2026/vol-57-no-1-april/science-fiction-prototyping/README.md) – Julian Pakay¹ and Evie Kendal²
- [Hit Play Before You Pipette: Pre-laboratory Videos to Boost Biochemistry Practicals](2026/vol-57-no-1-april/hit-play-before-you-pipette/README.md) – David Leaver and Doaa Hanafy
- [Sketching Science: Graphical Abstracts as an Authentic Assessment](2026/vol-57-no-1-april/sketching-science-graphical-abstracts-as-an-authentic-assessment/README.md) – Katrina Binger¹,², Maria Demaria³ and Mark Wright³

### [August 2026 – Vol 57 No 2](2026/vol-57-no-2-august/README.md)

- [Building Stronger Biochemistry Educators Nationwide: Early Impact of the ASBMB Education SIG Peer Mentoring Program](2026/vol-57-no-2-august/peer-mentoring-program/README.md) – Amber Willems-Jones on behalf of the ASBMB Education SIG
- [A Picture is Worth 1,000 Words – What is a Video Worth? Student Perceptions of Video and Screen-recorded Feedback](2026/vol-57-no-2-august/video-feedback/README.md) – James Tsatsaronis
- [Scaling Engagement in Large Biochemistry Classes: A Case-based Redesign Using Digital Collaboration to Maintain Learning Quality](2026/vol-57-no-2-august/scaling-engagement/README.md) – Mehrnaz Keyhanfar, Briony Forbes and Amy Wyatt
- [Taking ASBMB Education to Europe: Report on the FEBS Education and Training Conference](2026/vol-57-no-2-august/febs-education-conference/README.md) – Nirma Samarawickrema

## GitHub Pages copy

`site/build.py` publishes the website pages described below outside the ASBMB website, with the ASBMB layout unchanged. The home page is the Australian Biochemist Education Feature page (`templates/asbmb-education-feature-page.html`) with the article list from `website/education-page-article-links.html` added after its Contributing section, and each article is its `education-feature-<article-slug>.html` page. To make the pages work away from www.asbmb.org.au, the script removes their `<base>` element so images load from each article's `images/` folder and points the site menu at the matching pages on www.asbmb.org.au. The menu's Australian Biochemist Education Feature link, and each article's "< Back to Education" link, go to the home page. The files in this repository are not changed.

To build it locally (Python 3, no extra packages):

```
python3 site/build.py          # writes the site to _site/
```

Then open `_site/index.html` in a browser.

The workflow in `.github/workflows/pages.yml` builds the site and publishes it with GitHub Pages on every push to `main`. To turn it on, go to **Settings → Pages** and set **Source** to **GitHub Actions**.

## Using the website pages

The `education-feature-*.html` files use the same header, footer and styles as the Education page (`templates/asbmb-education-page.html`), and the site menu from the Australian Biochemist Education Feature page (`templates/asbmb-education-feature-page.html`), where Education is a drop-down that includes the Education Feature page. The article title is the page heading, body text and tables use the site's 15px body style, and each page ends with a note on where the article first appeared and a link back to Education.

- **Images.** Pages refer to images as `images/<file>`. The template sets `<base href="https://www.asbmb.org.au/">`, so on the live site these paths resolve against the site root. Before publishing, upload each article's images (for example to the EventsAir file store) and replace the `src` paths with the uploaded URLs. Opened locally, the pages show their text but not their images or site styling.
- **Page addresses.** Canonical and social-media URLs assume each page is published at `https://www.asbmb.org.au/education-feature-<article-slug>`. Change them if the site uses different page names.
- **Links from the Education Feature page.** `website/education-page-article-links.html` lists every article page, grouped by issue, under an Education Feature Articles heading styled like the Contributing heading on the Australian Biochemist Education Feature page (`templates/asbmb-education-feature-page.html`). Paste it after that page's Contributing section.

## How the articles were prepared

The text was extracted from the high- and low-resolution PDFs of each issue and checked against the printed layout. The wording is as published. The only changes are these:

- **Layout repairs.** Paragraphs split across columns, pages or figures were rejoined, and hyphens from line breaks were removed. Captions, author biographies and reference lists were reassembled, and hyperlinks embedded in the PDFs were kept.
- **Figures drawn as vector graphics** were rendered from the PDF as images. This applies to flow diagrams, reaction schemes, charts, figure panels made of several pieces, and groups of portrait photos.
- **Not included:** advertisements and notices that shared pages with the Education Feature, the coordinator line at the start of each feature (listed on each issue page instead), and the obituary for John Wallace that appeared on the same page as the April 2025 feature.
- **Tables** were rebuilt as text tables. In *Getting to the CoRe of Flow Cytometry* (August 2025), Table 3's colour key could not be kept, so each row is labelled with its knowledge type instead.
- **Typographical corrections**, where the printed text had an obvious slip:
  - *A Picture is Worth 1,000 Words* (Aug 2026): “Students three main themes” → “Students identified three main themes”
  - *Using Digital Technologies to Create an Engaging Small Group Learning Experience* (Aug 2022): “efforts efforts” → “efforts”
  - *Building Career-ready Scientists* (Dec 2024): “comprared” → “compared” (Fig. 1 caption)
  - *Using an Assessment Literacy Module* (Apr 2024): “0 .086” → “0.086” (Table 1)
  - *Educator and Student Reflections on Supervising and Conducting Biochemistry Education-based Research* (Aug 2024): “coming form” → “coming from”
  - *On the Fly* (Apr 2022): the asterisk used as a footnote marker in the Fig. 1 caption is shown as †
- **Updates after publication:**
  - *Preparing the Next Generation of Students for AI-Driven Biomedical Research* (Aug 2025): Fig. 1 is placed under the paragraph that cites it, and a footnote added at the first mention of ProteinDJ says the ProteinDJ work has since been published (*Protein Science* 2026, 35(2):e70464) and is available online.
  - *Educator and Student Reflections on Supervising and Conducting Biochemistry Education-based Research* (Aug 2024): author corrections from Jordan Witchard to his answers: “Biochemistry and Genetics” → “biochemistry and genetics”; “First year” → “first-year”; “literature as I found myself” → “literature. I found myself”; “understand, i.e. effect” → “understand such as effect”; “learned, I have turned” → “learned. I have turned”.

All other spelling and wording, including inconsistencies in the original, has been left as printed.

## Copyright

© Australian Society for Biochemistry and Molecular Biology Inc. All articles were first published in the *Australian Biochemist*. Copyright in the articles and images remains with the ASBMB and the authors. This repository is an archival copy, and it should stay private unless the ASBMB agrees otherwise.
