// Everything the /work pages read from work.md and homepage.md, resolved once so the
// section components, the hub, the single-scroll view and the case pages agree.
import { loadPage, statPairs } from './page.mjs';
import { loadHomepage, parseKV, paragraphs, bullets } from './homepage.mjs';

// The route map. Slugs are public URLs: renaming one breaks a link.
export const CASES = [
  { n: 1, slug: 'design-organisation', og: '/video/txd-poster.jpg' },
  { n: 2, slug: 'mytoyota-lexus', og: '/images/work/myt-hand.jpg' },
  { n: 3, slug: 'songkick-dopay', og: '/images/work/songkick-live.jpg' },
  { n: 4, slug: 'ai-products', og: '/images/work/emotrix-timeline.jpg' },
];
export const PROJECTS = [
  { key: 'prepcall', slug: 'prepcall' },
  { key: 'emotrix', slug: 'emotrix' },
  { key: 'nudge', slug: 'nudge' },
];
export const caseHref = (n) => `/work/${CASES[n - 1].slug}/`;

export function loadWork() {
  const { meta, sections } = loadPage('work.md');
  const S = (k) => sections[k] || '';
  const P = (k) => paragraphs(S(k));
  const lead = (b) => { const m = b.match(/^\*\*(.+?)\*\*\s*(.*)$/s); return m ? { lead: m[1], body: m[2] } : { lead: '', body: b }; };
  const B = (k) => bullets(S(k)).map(lead);
  const c = (n) => ({ info: parseKV(S(`case${n}-meta`)), stats: statPairs(S(`case${n}-stats`)) });
  const c1 = c(1), c2 = c(2), c3 = c(3), c4 = c(4);

  const intro = P('intro');
  const narr = P('case1-narrative');
  const turnIdx = narr.findIndex((p) => p.startsWith('Service design came out of'));
  const creditIdx = narr.findIndex((p) => p.startsWith('What they went on to build'));
  const narr3a = narr[creditIdx - 1];
  const narr3b = narr[creditIdx];
  const commercial = P('case1-commercial')[0];
  const com1 = commercial.split('. I ran')[0] + '.';
  const com2 = 'I ran' + commercial.split('. I ran')[1];
  const role2 = P('case2-role');
  const hard2 = P('case2-hard');
  const closing = P('closing');
  const contact = P('contact');

  const gaugeCards = [
    ['Case one', 'The organisation', c1.info, 'Everything here is mine. Built from nothing, run for seven years, sold engagement by engagement.', 'amber', 'fill'],
    ['Case two', 'What the organisation shipped', c2.info, 'The team I had built was already in place, run by two design managers with the client\'s trust.', 'teal', 'ring'],
    ['Case three', 'Two products, two markets', c3.info, 'Eight years at Songkick from seed to the Warner Music Group acquisition, then Dopay from concept to a live service. On both I designed the product myself and built the design team around it.', 'amber', 'fill'],
    ['Case four', 'Two AI products, built alone', c4.info, 'PrepCall, an AI voice coach I designed, built and shipped myself. Emotrix, the interpretation layer that came out of it, now in a live pilot under NDA.', 'ink', 'fill'],
  ];
  const gov = [
    ['EU AI Act, Article 5', 'Classification and the data protection impact assessment, on a shipped product'],
    ['European Accessibility Act', 'Governance across a whole design function, turned into a four-tier service'],
    ['Regulated delivery', 'Every programme in the first two cases, and Dopay as a regulated payments product in Egypt'],
  ];
  const colour = { amber: 'var(--amber)', teal: 'var(--teal)', ink: 'var(--ink)' };

  const home = loadHomepage().sections;
  const projects = PROJECTS.map((p) => ({ ...p, ...parseKV(home[`project-${p.key}`] || '') }));

  return { meta, sections, S, P, B, c1, c2, c3, c4, cases: [c1, c2, c3, c4], intro, narr, turnIdx, creditIdx, narr3a, narr3b, com1, com2, role2, hard2, closing, contact, gaugeCards, gov, colour, projects };
}
