---
title: After the App Grid
subtitle: On generative interfaces, the slow death of a fifteen year old assumption, and what design leadership should actually do about it.
category:
  - Design
  - AI
readTime: 5 min read
image: images/article-10.png
featured: true
---
For the last fifteen years, almost every app on the home screen has shared the same shape. A grid of icons. A tab strip at the bottom. A search field at the top. The arrangement is so consistent that most people have stopped noticing it.

That arrangement is, finally, being questioned in a way that warrants attention.

Felix Haas published a piece this week titled "Generative Interfaces" that articulates something a lot of people have been circling around. Apps, he argues, were a workaround. They existed because software could not understand us, so we adapted to it instead. With language models that can hold real context, the case for fifty separate containers, each with its own learning curve and its own opinions about how you should hold it, gets harder to defend.

> "Apps were built for a world where software couldn't understand you. That world is over."
> Felix Haas

He is not the first person to make this case. Paul Adams at Intercom has been writing about "the end of apps as we know them" for the better part of a decade. Carl Pei at Nothing just published a video laying out a phone OS built around the same instinct, a home screen that surfaces context rather than containers. Vercel has shipped tooling that lets language models render functional UI on the fly rather than just describing it in text. Researchers at Ink & Switch have been writing about "malleable software" for years. Geoffrey Litt has been arguing that LLMs let users spin up disposable, single-purpose micro-apps that exist for an hour and then disappear. Rabbit's "Large Action Model" framing made the same argument from the device side: the AI uses the apps, the user does not.

So this is not new thinking. What is new is that the technology might finally be catching up.

## We have been here before

I have lived through enough platform shift predictions to be cautious. In 2016 I wrote a piece naming chatbots, VR, and the Internet of Things as the things to watch. Bots were going to be the new browsers. VR was about to "end the screen age." Connected things were about to dissolve into the background of everyday life. Some of that landed. Most of it arrived later, quieter, and less consequentially than anyone forecast.

The "death of the app" prediction is not new either. It has been showing up in trade press since at least 2014. Every couple of years someone writes a piece arguing that the operating system, or the assistant, or the browser, is about to absorb the apps and free us from the grid. It has not happened. The home screen is still a grid.

So my first instinct, when I read pieces like the one Haas wrote, is to slow down and ask what is actually different this time.

## What is actually different

Two things, I think.

The first is that the missing piece, software that can understand intent expressed in natural language, has actually arrived. Not perfectly, not consistently, not for every domain. But well enough that the basic thesis no longer requires a leap of faith.

The earlier predictions failed for different reasons. VR ran into hardware, content, and motion sickness. IoT got there, but quietly. The chatbot prediction failed for one specific reason: the language layer was brittle. Bots in 2016 were search bars with worse UX. The interface was conversational; the comprehension was not. That is the part that has shifted.

The second is the collapse in the cost of producing software. I wrote about this in "Discovery is not dead." When the cost of making something real drops by an order of magnitude, the assumption that you need polished, pre-fabricated containers to be useful starts to look strange. If a workable interface can be generated on demand, in milliseconds, around the specific task in front of you, the case for downloading, learning, and tolerating someone else's compromises gets weaker.

These two shifts are pulling in the same direction. One says the system can finally understand what you want. The other says the system can finally produce, on the spot, what you need to do it. Together, they put real pressure on the grid.

## Where this changes the design problem

I want to take Haas's argument and push on it a bit, because the part that interests me most is the one he raises near the end and then does not fully answer.

If interfaces are generated on demand, the locus of design shifts. You are no longer designing screens. You are designing the system that decides what to render, when, with what affordances, and for whom.

That is a different discipline. It is closer to systems design than to interface design as I have practised it for thirty years. It cares less about the placement of a button and more about the rules that govern when a button appears at all. It cares less about the visual hierarchy of a screen and more about the principles the model uses to decide what to surface.

There are at least three problems in this direction that nobody has solved cleanly yet.

The first is consistency. Static interfaces have a kind of forgiving consistency baked in. The button is in the same place because someone designed it that way and shipped it. A generative interface offers no such guarantee. The same task, performed twice, may render differently. That has implications for learnability, for trust, and for accessibility that are not trivial. Users build muscle memory. Generative interfaces, if they are not carefully constrained, undermine it.

The second is trust, which Haas does name. If the system is choosing what to show me, I need to understand what it knows and how it is deciding. The history of recommendation systems is not encouraging here. Most of the consumer-grade ones operate as black boxes, and we have all learned to be slightly suspicious of them. Trust in a generative interface will need to be designed for explicitly. It is not going to emerge from the technology on its own.

The third is the loss of the brand surface. For decades, the interface was where a product established its character. The voice, the tone, the small decisions that signal you are using this thing rather than that thing. If interfaces are generated on demand, where does brand actually live? In the prompt? In the model's training? In a style system the model is required to respect? I do not think anyone has a good answer yet, and I suspect those answers will turn out to matter more than people are currently assuming.

## What this asks of design leadership

For anyone running a design team right now, the practical question is what to do with any of this.

I would not, on the basis of a few interesting essays and one Nothing video, restructure your team around generative interfaces tomorrow. The hype cycle is just getting started. Most products that ship a "generative interface" in the next twelve months will be putting a chat bot on top of their existing product and calling it a transformation. A lot of confident predictions are about to be wrong.

What I would do is start asking different questions in your discovery work.

What does the model need to know about the user to be useful? Where does that data live, and is it actually accessible? Where would rendering an interface on demand genuinely beat a pre-built screen, and where would it be slower, weirder, or more confusing? What standards do you want the system to hold itself to, and how would you enforce them? What is your failure mode when the model gets it wrong, and is that failure mode one you can live with?

I would also start treating context as a first-class design material. The whole generative interface story rests on the system having the right context at the right time. That is not really a model problem. It is a data, integration, and consent problem, and most organisations are nowhere near ready for it. The companies that get this right will be the ones that have done the unglamorous work on identity, preferences, and signals long before they ever try to render an interface on the fly.

This connects back to something I keep coming back to. The bottleneck is shifting from making things to deciding what is worth making. From producing artefacts to exercising judgment. From shipping screens to shaping the system behind them. Generative interfaces accelerate that shift. They do not introduce it.

## The longer view

I started by saying the home screen is still a grid. It is. And it might be a grid for some time yet. Platform shifts of this kind almost always take longer than the people writing about them suggest, and the transition is rarely as clean as the manifestos imply. We will probably end up with a hybrid for years. Some things will become generative; many will not. Apps will not vanish overnight, and the ones that survive will be the ones that genuinely benefit from being a place rather than a response.

But the underlying point Haas is making, that the app was a workaround for a limitation that has now been removed, is right. The grid will not go away tomorrow. The thinking behind it has already started to shift, and that shift will play out over years.

The work for designers and design leaders, in the meantime, is what it has always been. Pay attention to what the technology actually enables. Separate the real signal from the marketing. Take the design problems that the new capability creates seriously, especially the unsexy ones around trust, consistency, and accountability. And do not get carried away by the people claiming certainty too early.

Generative interfaces are coming. Some of them will be brilliant, and a lot of them will be bad. Most of the design work is still ahead of us.

---

*Written in response to Felix Haas's "Generative Interfaces" (May 2026), with reference to Paul Adams (Intercom), Carl Pei (Nothing), Vercel's Generative UI work, Ink & Switch on malleable software, and Geoffrey Litt on LLM-driven micro-apps.*
