import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// Frontmatter is inconsistent across the ten articles (see CLAUDE.md):
// category may be a string or an array (normalised to array here),
// subtitle may be empty (YAML null), featured is absent on most files.
// `order` preserves the display order previously encoded in articles.js.
const writing = defineCollection({
  loader: glob({ pattern: '[^_]*.md', base: './src/content/writing' }),
  schema: z.object({
    title: z.string(),
    subtitle: z
      .string()
      .nullable()
      .optional()
      .transform((v) => v ?? ''),
    category: z
      .union([z.string(), z.array(z.string())])
      .transform((v) => (Array.isArray(v) ? v : [v])),
    readTime: z.string(),
    image: z.string(),
    featured: z.boolean().optional().default(false),
    order: z.number(),
  }),
});

export const collections = { writing };
