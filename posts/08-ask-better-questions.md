---
title: Your AI Has Better Ideas Than It's Telling You
subtitle:
category:
  - AI
readTime: 6 min read
image: images/article-08.png
featured: true
---
Stanford published a research paper late last year that quietly reframed how I think about working with AI. No new model. No fine-tuning breakthrough. Just an observation about a flaw in how language models are trained, and a surprisingly simple fix.

The technique is called Verbalised Sampling. And it has changed the way I prompt Claude.

## The problem: mode collapse

When companies like Anthropic, OpenAI and Google train their models, the process happens in two phases. First, pretraining: the model learns from vast amounts of diverse text. At this stage, it is creative, unpredictable, and full of range.

Then comes alignment. The model is fine-tuned using human feedback to make it helpful and safe. Human raters evaluate outputs and consistently prefer responses that sound familiar. Typical. Safe.

Over time, this compresses the model's output range. The diversity from pretraining is still there, but it gets buried. The model learns to default to the most statistically average response every time. The Stanford researchers call this mode collapse.

You have probably experienced this yourself. Ask an AI to give you five ideas for something and you get five minor variations on the same idea. Change the wording. Raise the temperature. Add more context. Nothing meaningfully shifts. The model keeps serving the median.

The paper's key contribution is identifying why this happens at the data level: human annotators exhibit what the researchers call typicality bias. They systematically prefer text that sounds familiar. This is not a flaw in any specific model. It is a structural feature of how alignment training works.

## What the researchers found

The paper introduces a technique called Verbalized Sampling. The core idea: instead of asking the model for a single response, you ask it to generate multiple responses with their probabilities.

That sounds simple, and it is. But the reason it works is specific. Different prompts cause the model to collapse to different modes. When you ask for one answer, the model targets the most typical response. When you ask it to verbalise a probability distribution over multiple responses, it targets a different mode entirely: one that approximates the full range of outputs learned during pretraining. The diversity resurfaces not because you are asking nicely, but because you have changed which internal distribution the model is aiming at.

The researchers' own recommended prompt instructs the model to generate five responses, each with a probability, and to sample from the tails of the distribution so that no single response dominates. That tail-sampling constraint is what forces the model away from its default. Without it, you still get five responses that cluster around the same safe centre.

In their experiments across creative writing, dialogue simulation, open-ended question answering, and synthetic data generation, the technique produced between 1.6 and 2.1 times more diverse outputs than standard prompting. They also found that larger, more capable models benefit more, because they have more suppressed diversity to recover.

The paper is here: [Verbalized Sampling — arXiv:2510.01171](https://arxiv.org/abs/2510.01171)

The researchers have also published their code, datasets, and prompt templates on GitHub: [CHATS-lab/verbalized-sampling](https://github.com/CHATS-lab/verbalized-sampling)

## What this means in practice

This is not a magic trick. It is a shift in mental model.

Traditional prompt engineering optimises for control. More constraints. Tighter instructions. Specific formatting. That approach works when you know exactly what you want. But when you are exploring, whether that is strategic options, creative directions, or ways to frame a problem, over-constraining the model kills the thing you actually need: genuine diversity of thought.

Verbalised Sampling flips the approach. Instead of telling the model what to think, you give it room to show you what it knows. The quality of the output does not come from more precise instructions. It comes from a better question.

I have found this particularly useful in a few areas of my own work:

**Strategic thinking.** When exploring positioning for a new venture, asking for a distribution of approaches with confidence weightings surfaces directions I would not have considered. The model stops giving me the consensus answer and starts showing me the full landscape.

**Creative work.** For side projects where I need genuinely different concepts, not five variations on the same safe idea, verbalised sampling opens up the range significantly.

**Interview and job search preparation.** Asking for a distribution of framings for how to present experience, with probability weightings, produces less generic angles that cut through better.

**Multi-agent AI experiments.** If you are running agent architectures where different AI personas are supposed to offer distinct perspectives, injecting verbalised sampling into the prompt layer produces more genuinely divergent thinking rather than superficial variation.

## A Claude skill for Verbalised Sampling

I liked this technique enough that I built it into a reusable Claude skill. Skills are instruction packages that Claude loads automatically when they are relevant to what you are asking. You install them once and they work across all your conversations.

### The skill I have built does the following:

When you activate it, Claude first internally identifies what its default single response would have been. This creates an anchor to deliberately diverge from. It then generates five distinct responses, using the paper's tail-sampling method internally to force itself away from the dominant mode. The probabilities do their work during generation, shifting which internal distribution the model targets, but they are not displayed in the output. You just see the results: five genuinely different directions, each with enough substance to evaluate.

The format adapts to what you are asking. Strategic questions produce named approaches with trade-offs. Creative questions produce distinct concepts with enough detail to evaluate. Analytical questions produce competing hypotheses with supporting reasoning. The skill does not force every question into the same rigid template.

The skill does not end by collapsing back to a single recommendation. That would reintroduce the mode collapse the technique is designed to overcome. Instead, it closes by highlighting which responses represent the most different directions from each other, and what you might want to consider when choosing between them. The decision space stays open.

The skill is manual-only. It does not activate automatically. I deliberately set it up this way because the whole point of verbalized sampling is intentional divergence. You reach for it when you want the full landscape of options, not as a default filter on every conversation. Most of the time, a single considered response is exactly what you need. This is a power tool, not a mode.

## Before you start

You will need:

- A Claude Pro, Max, Team, or Enterprise subscription.
- The `.skill` file downloaded to your computer.

## Installing in the Claude desktop app

1. Open the Claude desktop app.
2. Go to **Settings** (click your profile icon, then select Settings).
3. Navigate to **Capabilities** and make sure **Code execution and file creation** is toggled on. Skills require this to work.
4. Navigate to **Customize**, then select **Skills**.
5. Click the **+** button, then select **Upload a skill**.
6. Choose the `.skill` file you downloaded.
7. The skill will appear in your skills list. Make sure the toggle is on.

You are done. The skill is now active across all your conversations.

That is it. It works across all your conversations from that point, whether you are using the web app or the desktop app.

## How to use it

Add **"use VS"** or **"VS mode"** to any prompt where you want the verbalised sampling pattern applied.

For example: "What should I prioritise in my first 90 days as a design director? Use VS."

Claude will respond with five distinct options, each with a descriptive name and enough detail to evaluate, formatted appropriately for the type of question you have asked. It will close by mapping the decision space rather than picking a winner for you.

You can also say "verbalised sampling" or "give me diverse options with probabilities" if you prefer to be more explicit. The skill recognises all of these phrases.

## When to use it

Use it when you are exploring, not executing. Strategy sessions. Creative briefs. Career decisions. Brainstorming. Anywhere you want the full landscape of options rather than the model's safest guess.

Do not use it when you need a specific, correct answer, when you are debugging code, or when you explicitly want Claude to just tell you what to do. In those cases, single-path generation is better.

## The bigger point

Prompt engineering is not dead. But the mental model behind it has shifted. For the last couple of years, the instinct has been to write longer, more constrained prompts. More context. More rules. More formatting instructions. That was compensating for a problem we did not fully understand.

The models were never uncreative. They were over-aligned, trained to suppress the range that made them powerful. Verbalised sampling does not rewrite the model. It just gives it permission to show you what it already knows.

Sometimes, the best way to get better output from AI is not to write a better instruction. It is to ask a better question.

---

_Gideon Bullock is a design leader with 25 years of experience building and scaling design organisations inside product and engineering teams. He writes about design leadership, AI-assisted creativity, and how work actually happens inside organisations._