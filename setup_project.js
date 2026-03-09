#!/usr/bin/env node
'use strict';

const fs = require('fs');
const path = require('path');

const PROJECT_NAME = 'NET3006A-ML-Network-Telemetry';
const ROOT = path.join(__dirname, PROJECT_NAME);

function ensureDir(dir) {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
    return true;
  }
  return false;
}

function writeIfNotExists(filePath, content) {
  if (!fs.existsSync(filePath)) {
    fs.writeFileSync(filePath, content);
    return true;
  }
  return false;
}

function writeFile(filePath, content) {
  const dir = path.dirname(filePath);
  ensureDir(dir);
  return writeIfNotExists(filePath, content);
}

const FILES = {
  'package.json': `{
  "name": "net3006a-ml-network-telemetry",
  "version": "1.0.0",
  "description": "NET3006A Survey Project - ML for Network Telemetry",
  "private": true,
  "dependencies": {
    "docx": "^9.6.0"
  }
}
`,

  'README.md': `# NET3006A Project — ML for Network Telemetry

**Course:** NET3006A — Network Management and Machine Learning, Carleton University (Winter 2026)
**Instructor:** Dr. Jie Gao
**Option:** Survey / Reading (Option 1)
**Topic:** Topic 2 – ML for Network Telemetry

## Team
- Abdul Rehman — ML methods for anomaly detection
- Esam Mukbil — ML for performance prediction & QoS
- Hashim Kshim — Industry implementations & emerging trends (6G, GenAI)

## Project Structure
- \`proposal/\` — Submission proposal and generator script
- \`papers/\` — All PDF references (must be annotated for submission)
- \`notes/\` — Individual reading notes per team member
- \`synthesis/\` — Shared synthesis documents
- \`presentation/\` — Presentation outline and individual slide folders
- \`references/\` — Full bibliography

## Getting Started
1. Run \`node proposal/generate_proposal.js\` to regenerate the proposal docx
2. Add annotated PDFs to \`papers/\` as you find them
3. Take notes in your folder under \`notes/\`
4. Update \`synthesis/key_findings.md\` as a team after each sync
`,

  'proposal/generate_proposal.js': getGenerateProposalContent(),

  'papers/README.md': `# Papers

Store all PDF references here. **Important:** Annotate each PDF before final submission.
`,

  'papers/.gitkeep': '',

  'notes/README.md': `# Reading Notes

Each team member maintains one notes file per paper or sub-topic in their folder.
`,

  'notes/abdul/anomaly_detection_notes.md': `# Anomaly Detection in Network Telemetry — Reading Notes
**Owner:** Abdul Rehman

## Papers to Read
- [ ] (add paper titles here)

## Notes Template

### Paper: [Title]
- **Source:**
- **Key ML Method:**
- **Telemetry Task:**
- **Key Finding:**
- **Limitations:**
`,

  'notes/esam/performance_prediction_notes.md': `# Performance Prediction & QoS — Reading Notes
**Owner:** Esam Mukbil

## Papers to Read
- [ ] (add paper titles here)

## Notes Template

### Paper: [Title]
- **Source:**
- **Key ML Method:**
- **Telemetry Task:**
- **Key Finding:**
- **Limitations:**
`,

  'notes/hashim/industry_trends_notes.md': `# Industry Implementations & Emerging Trends — Reading Notes
**Owner:** Hashim Kshim

## Sources to Read
- [ ] Modern Broadband Network Telemetry (Nokia)
- [ ] From data mess to AI-ready data mesh (Ericsson)
- [ ] Visualizing network performance: Ericsson's Transport Automation Controller with AI/ML
- [ ] 6G Network Architecture: QoS Paradigms and Data Lifecycle Management
- [ ] Mobile Network Data Synthesis with Generative AI

## Notes Template

### Source: [Title]
- **Publisher:**
- **Key ML/AI Approach:**
- **Telemetry Use Case:**
- **Key Takeaway:**
`,

  'synthesis/README.md': `# Synthesis Documents

Shared team synthesis. Update collaboratively after each sync.
`,

  'synthesis/key_findings.md': `# Key Findings — ML for Network Telemetry

> Updated collaboratively after each team sync.

## ML Methods Observed
| Method | Papers/Sources | Telemetry Task |
|--------|---------------|----------------|
| | | |

## Common Themes


## Surprises / Contradictions


## Gaps in the Literature
`,

  'synthesis/ml_methods_summary.md': `# ML Methods Summary

| ML Method | Category | Papers Using It | Telemetry Task | Performance Noted |
|-----------|----------|----------------|----------------|------------------|
| | | | | |
`,

  'synthesis/open_challenges.md': `# Open Challenges & Future Directions

## Identified Challenges
1.

## Emerging Trends
1.

## Our Team's Perspective
`,

  'presentation/README.md': `# Presentation

Slides and outline for the final presentation.
`,

  'presentation/outline.md': `# Presentation Outline
**Duration:** 15 minutes presentation + 5 minutes Q&A
**Rule:** Each presenter's name must appear on every slide they present.
**Rule:** Each presenter must create their own slides without help from others.

## Suggested Structure

1. **Introduction & Motivation** — Abdul (~3 min)
   - What is network telemetry?
   - Why apply ML to it?
   - Scope of this survey

2. **ML Methods for Anomaly Detection** — Abdul (~3 min)
   - Methods found, datasets used, results

3. **ML for Performance Prediction & QoS** — Esam (~4 min)
   - Methods found, key papers, findings

4. **Industry Implementations & Emerging Trends** — Hashim (~3 min)
   - Nokia, Ericsson, 6G context, GenAI

5. **Conclusion & Key Takeaways** — Hashim (~2 min)
   - Summary, open challenges, what we learned

## Q&A Prep
- Each member prepares 2–3 potential questions on their section
`,

  'presentation/abdul_slides/.gitkeep': '',
  'presentation/esam_slides/.gitkeep': '',
  'presentation/hashim_slides/.gitkeep': '',

  'references/README.md': `# References

Full bibliography in references.md. All PDFs must be in papers/ and annotated.
`,

  'references/references.md': `# References

> Format: IEEE or APA. List all papers, articles, and reports surveyed.
> All PDFs must be saved in \`papers/\` and annotated before final submission.

## Academic Papers
1.

## Industry Reports / White Papers
1. Nokia — Modern Broadband Network Telemetry
2. Ericsson — From data mess to AI-ready data mesh
3. Ericsson — Visualizing network performance: Transport Automation Controller with AI/ML
4. iTeleScope: Softwarized Network Middle-Box for Real-Time Video Telemetry and Classification

## Datasets / Benchmarks
1.
`,
};

function getGenerateProposalContent() {
  const sourcePath = path.join(__dirname, 'proposal', 'generate_proposal.js');
  if (fs.existsSync(sourcePath)) {
    return fs.readFileSync(sourcePath, 'utf8');
  }
  return `const {
  Document,
  Packer,
  Paragraph,
  TextRun,
  Table,
  TableRow,
  TableCell,
  AlignmentType,
  BorderStyle,
  WidthType,
  ShadingType,
  TableLayoutType,
  convertInchesToTwip,
} = require('docx');
const fs = require('fs');
const path = require('path');

const FONT = 'Arial';
const BODY_SIZE = 22;
const HEADER_SIZE = 24;

const tableData = [
  ['Topic scoping & initial paper search', 'Week 1 (Mar. 10–14)', 'All members'],
  ['Read & annotate 2–3 papers each', 'Week 2 (Mar. 17–21)', 'Abdul, Esam, Hashim'],
  ['Synthesize findings & outline presentation', 'Week 3 (Mar. 24–28)', 'All members'],
  ['Draft presentation slides (each member\\'s section)', 'Week 4 (Mar. 31–Apr. 4)', 'Each member owns their slides'],
  ['Internal rehearsal & Q&A prep', 'Week 5 (Apr. 7–11)', 'All members'],
  ['Final submission of slides on Brightspace', 'Night before presentation', 'Abdul (submitter)'],
];

const headerRow = ['Step / Milestone', 'Target Date', 'Responsible Member'];

function createTableCell(text, options = {}) {
  return new TableCell({
    width: options.width ? { size: options.width, type: WidthType.DXA } : undefined,
    shading: options.shading ? { fill: options.shading, type: ShadingType.CLEAR } : undefined,
    margins: options.margins || { top: 80, bottom: 80, left: 120, right: 120 },
    children: [
      new Paragraph({
        children: [
          new TextRun({
            text,
            font: FONT,
            size: options.bold ? HEADER_SIZE : BODY_SIZE,
            bold: options.bold,
          }),
        ],
        alignment: options.alignment,
      }),
    ],
  });
}

function createTable() {
  const rows = [
    new TableRow({
      tableHeader: true,
      children: headerRow.map((text, i) => {
        const widths = [4200, 2160, 3000];
        return createTableCell(text, { width: widths[i], shading: 'D5E8F0', bold: true });
      }),
    }),
    ...tableData.map(row =>
      new TableRow({
        children: row.map((text, i) => {
          const widths = [4200, 2160, 3000];
          return createTableCell(text, { width: widths[i] });
        }),
      })
    ),
  ];
  return new Table({
    layout: TableLayoutType.FIXED,
    width: { size: 9360, type: WidthType.DXA },
    rows,
  });
}

const doc = new Document({
  styles: { default: { document: { run: { font: FONT, size: BODY_SIZE } } } },
  sections: [{
    properties: {
      page: {
        margin: {
          top: convertInchesToTwip(1),
          right: convertInchesToTwip(1),
          bottom: convertInchesToTwip(1),
          left: convertInchesToTwip(1),
        },
      },
    },
    children: [
      new Paragraph({
        children: [new TextRun({ text: 'NET3006A Project Proposal — ML for Network Telemetry', font: FONT, size: HEADER_SIZE, bold: true })],
        alignment: AlignmentType.CENTER,
        border: { bottom: { color: '2E75B6', space: 1, style: BorderStyle.SINGLE, size: 6 } },
      }),
      new Paragraph({ text: '', spacing: { after: 200 } }),
      new Paragraph({ children: [new TextRun({ text: '1. Team Members', font: FONT, size: HEADER_SIZE, bold: true })] }),
      new Paragraph({ children: [new TextRun({ text: 'Abdul Rehman', font: FONT, size: BODY_SIZE })], bullet: { level: 0 } }),
      new Paragraph({ children: [new TextRun({ text: 'Esam Mukbil', font: FONT, size: BODY_SIZE })], bullet: { level: 0 } }),
      new Paragraph({ children: [new TextRun({ text: 'Hashim Kshim', font: FONT, size: BODY_SIZE })], bullet: { level: 0 } }),
      new Paragraph({ text: '', spacing: { after: 150 } }),
      new Paragraph({ children: [new TextRun({ text: '2. Project Option', font: FONT, size: HEADER_SIZE, bold: true })] }),
      new Paragraph({ children: [new TextRun({ text: 'Option 1: Survey / Reading Project', font: FONT, size: BODY_SIZE })] }),
      new Paragraph({ children: [new TextRun({ text: 'The team will survey and synthesize recent academic and industry literature on the use of machine learning for network telemetry.', font: FONT, size: BODY_SIZE })] }),
      new Paragraph({ text: '', spacing: { after: 150 } }),
      new Paragraph({ children: [new TextRun({ text: '3. Topic', font: FONT, size: HEADER_SIZE, bold: true })] }),
      new Paragraph({ children: [new TextRun({ text: 'Topic 2 – ML for Network Telemetry', font: FONT, size: BODY_SIZE })] }),
      new Paragraph({ children: [new TextRun({ text: 'Machine learning methods are increasingly being applied to automatically extract insights from high-volume, fine-grained network measurement data — such as flow statistics, packet traces, and in-band telemetry. This enables real-time anomaly detection, performance prediction, and autonomous network optimization. Our survey will examine how state-of-the-art ML techniques are applied across these sub-problems in modern network telemetry pipelines.', font: FONT, size: BODY_SIZE })] }),
      new Paragraph({ text: '', spacing: { after: 150 } }),
      new Paragraph({ children: [new TextRun({ text: '4. Project Objective', font: FONT, size: HEADER_SIZE, bold: true })] }),
      new Paragraph({ children: [new TextRun({ text: 'The objective of this project is to explore and synthesize the current state of research and industry practice in applying machine learning to network telemetry. Specifically, the team will: (1) identify and categorize the primary ML methods used (e.g., supervised, unsupervised, deep learning), (2) map them to specific network telemetry tasks such as anomaly detection, traffic prediction, and QoS optimization, and (3) identify open challenges and emerging trends in the field, particularly in the context of 5G/6G and next-generation network architectures.', font: FONT, size: BODY_SIZE })] }),
      new Paragraph({ text: '', spacing: { after: 150 } }),
      new Paragraph({ children: [new TextRun({ text: '5. Steps, Timeline, and Task Division', font: FONT, size: HEADER_SIZE, bold: true })] }),
      createTable(),
      new Paragraph({ text: '', spacing: { after: 150 } }),
      new Paragraph({ children: [new TextRun({ text: 'Task Division Summary:', font: FONT, size: BODY_SIZE, bold: true })] }),
      new Paragraph({ children: [new TextRun({ text: 'Abdul Rehman: ML methods for anomaly detection in telemetry; submission logistics', font: FONT, size: BODY_SIZE })], bullet: { level: 0 } }),
      new Paragraph({ children: [new TextRun({ text: 'Esam Mukbil: ML for performance prediction and QoS optimization', font: FONT, size: BODY_SIZE })], bullet: { level: 0 } }),
      new Paragraph({ children: [new TextRun({ text: 'Hashim Kshim: Industry implementations (Nokia, Ericsson) and emerging trends (6G, GenAI for telemetry)', font: FONT, size: BODY_SIZE })], bullet: { level: 0 } }),
    ],
  }],
});

async function main() {
  const buffer = await Packer.toBuffer(doc);
  const outputPath = path.join(__dirname, 'NET3006A_Project_Proposal.docx');
  fs.writeFileSync(outputPath, buffer);
  console.log('Created: ' + outputPath);
}

main().catch(console.error);
`;
}

function main() {
  const created = [];
  const skipped = [];

  ensureDir(ROOT);
  created.push(PROJECT_NAME + '/');

  for (const [relPath, content] of Object.entries(FILES)) {
    const fullPath = path.join(ROOT, relPath);
    if (writeFile(fullPath, content)) {
      created.push(relPath);
    } else {
      skipped.push(relPath);
    }
  }

  console.log('\n=== NET3006A Project Setup Complete ===\n');
  console.log('Created:');
  created.forEach((p) => console.log('  +', p));
  if (skipped.length > 0) {
    console.log('\nSkipped (already exist):');
    skipped.forEach((p) => console.log('  -', p));
  }
  console.log('\nNext steps:');
  console.log('  1. cd ' + PROJECT_NAME);
  console.log('  2. npm install');
  console.log('  3. node proposal/generate_proposal.js');
  console.log('');
}

main();
