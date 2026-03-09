const {
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
const BODY_SIZE = 22; // 11pt in half-points
const HEADER_SIZE = 24; // 12pt in half-points

const tableData = [
  ['Topic scoping & initial paper search', 'Week 1 (Mar. 10–14)', 'All members'],
  ['Read & annotate 2–3 papers each', 'Week 2 (Mar. 17–21)', 'Abdul, Esam, Hashim'],
  ['Synthesize findings & outline presentation', 'Week 3 (Mar. 24–28)', 'All members'],
  ['Draft presentation slides (each member\'s section)', 'Week 4 (Mar. 31–Apr. 4)', 'Each member owns their slides'],
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
        return createTableCell(text, {
          width: widths[i],
          shading: 'D5E8F0',
          bold: true,
        });
      }),
    }),
    ...tableData.map(
      (row) =>
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
  styles: {
    default: {
      document: {
        run: {
          font: FONT,
          size: BODY_SIZE,
        },
      },
    },
  },
  sections: [
    {
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
          children: [
            new TextRun({
              text: 'NET3006A Project Proposal — ML for Network Telemetry',
              font: FONT,
              size: HEADER_SIZE,
              bold: true,
            }),
          ],
          alignment: AlignmentType.CENTER,
          border: {
            bottom: {
              color: '2E75B6',
              space: 1,
              style: BorderStyle.SINGLE,
              size: 6,
            },
          },
        }),
        new Paragraph({ text: '', spacing: { after: 200 } }),
        new Paragraph({
          children: [
            new TextRun({ text: '1. Team Members', font: FONT, size: HEADER_SIZE, bold: true }),
          ],
        }),
        new Paragraph({
          children: [
            new TextRun({ text: 'Abdul Rehman', font: FONT, size: BODY_SIZE }),
          ],
          bullet: { level: 0 },
        }),
        new Paragraph({
          children: [
            new TextRun({ text: 'Esam Mukbil', font: FONT, size: BODY_SIZE }),
          ],
          bullet: { level: 0 },
        }),
        new Paragraph({
          children: [
            new TextRun({ text: 'Hashim Kshim', font: FONT, size: BODY_SIZE }),
          ],
          bullet: { level: 0 },
        }),
        new Paragraph({ text: '', spacing: { after: 150 } }),
        new Paragraph({
          children: [
            new TextRun({ text: '2. Project Option', font: FONT, size: HEADER_SIZE, bold: true }),
          ],
        }),
        new Paragraph({
          children: [
            new TextRun({ text: 'Option 1: Survey / Reading Project', font: FONT, size: BODY_SIZE }),
          ],
        }),
        new Paragraph({
          children: [
            new TextRun({
              text: 'The team will survey and synthesize recent academic and industry literature on the use of machine learning for network telemetry.',
              font: FONT,
              size: BODY_SIZE,
            }),
          ],
        }),
        new Paragraph({ text: '', spacing: { after: 150 } }),
        new Paragraph({
          children: [
            new TextRun({ text: '3. Topic', font: FONT, size: HEADER_SIZE, bold: true }),
          ],
        }),
        new Paragraph({
          children: [
            new TextRun({ text: 'Topic 2 – ML for Network Telemetry', font: FONT, size: BODY_SIZE }),
          ],
        }),
        new Paragraph({
          children: [
            new TextRun({
              text: 'Machine learning methods are increasingly being applied to automatically extract insights from high-volume, fine-grained network measurement data — such as flow statistics, packet traces, and in-band telemetry. This enables real-time anomaly detection, performance prediction, and autonomous network optimization. Our survey will examine how state-of-the-art ML techniques are applied across these sub-problems in modern network telemetry pipelines.',
              font: FONT,
              size: BODY_SIZE,
            }),
          ],
        }),
        new Paragraph({ text: '', spacing: { after: 150 } }),
        new Paragraph({
          children: [
            new TextRun({ text: '4. Project Objective', font: FONT, size: HEADER_SIZE, bold: true }),
          ],
        }),
        new Paragraph({
          children: [
            new TextRun({
              text: 'The objective of this project is to explore and synthesize the current state of research and industry practice in applying machine learning to network telemetry. Specifically, the team will: (1) identify and categorize the primary ML methods used (e.g., supervised, unsupervised, deep learning), (2) map them to specific network telemetry tasks such as anomaly detection, traffic prediction, and QoS optimization, and (3) identify open challenges and emerging trends in the field, particularly in the context of 5G/6G and next-generation network architectures.',
              font: FONT,
              size: BODY_SIZE,
            }),
          ],
        }),
        new Paragraph({ text: '', spacing: { after: 150 } }),
        new Paragraph({
          children: [
            new TextRun({ text: '5. Steps, Timeline, and Task Division', font: FONT, size: HEADER_SIZE, bold: true }),
          ],
        }),
        createTable(),
        new Paragraph({ text: '', spacing: { after: 150 } }),
        new Paragraph({
          children: [
            new TextRun({ text: 'Task Division Summary:', font: FONT, size: BODY_SIZE, bold: true }),
          ],
        }),
        new Paragraph({
          children: [
            new TextRun({ text: 'Abdul Rehman: ML methods for anomaly detection in telemetry; submission logistics', font: FONT, size: BODY_SIZE }),
          ],
          bullet: { level: 0 },
        }),
        new Paragraph({
          children: [
            new TextRun({ text: 'Esam Mukbil: ML for performance prediction and QoS optimization', font: FONT, size: BODY_SIZE }),
          ],
          bullet: { level: 0 },
        }),
        new Paragraph({
          children: [
            new TextRun({ text: 'Hashim Kshim: Industry implementations (Nokia, Ericsson) and emerging trends (6G, GenAI for telemetry)', font: FONT, size: BODY_SIZE }),
          ],
          bullet: { level: 0 },
        }),
      ],
    },
  ],
});

async function main() {
  const buffer = await Packer.toBuffer(doc);
  const outputPath = path.join(__dirname, 'NET3006A_Project_Proposal.docx');
  fs.writeFileSync(outputPath, buffer);
  console.log(`Created: ${outputPath}`);
}

main().catch(console.error);
