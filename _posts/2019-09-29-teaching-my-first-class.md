---
title: 'Some Thoughts from Teaching My First College Course'
tags: [General Science, Data & Technology]
status: publish
type: post
published: false
header:
  overlay_image: /assets/images/blog/2019-03-08-cosynesand.jpg
  overlay_filter: rgba(0,0,0,0.7)
  teaser: /assets/images/blog/2019-03-08-cosynesand.jpg
classes:
  - wide
permalink: /blog/:year/:month/:day/

excerpt: ""
---

As noted elsewhere on this website, I am very poor at forecasting how I will feel about something in the future. That's also how I stumbled into teaching an actual freaking college class this past summer. Earlier in the year, there was an opportunity to apply for this program at UCSD called **Summer Graduate Teaching Scholars (SGTS)**, where they pay you a little extra and give you a lot of training to teach your own course here. I thought, if there's some chance that I'd be a professional academic someday, maybe I should see how I like teaching an actual class, instead of just basing my experiences on TAing. Considering the extra money and the (very necessary) training, I was sold. What I clearly didn't consider in the sale was the absolute pandemonium that my summer would become as a result. This is the story of how I ended up teaching my own course for the first time ever on Neural Signal Processing.

This experience was up there for "hardest things I've ever done", in many ways. For one, I probably haven't consistently worked this many hours a week since the first two years of undergrad in Engineering Science. It was a rollercoaster ride that made 5 weeks seem like 5 months at times, but now that it's over, it felt like an instant. The harder part was coming to grips with the fact that 1) I have control over 33 people's grade for a senior-level class, which may have a real impact on their future job prospects, and 2) I have control over the technical content they walked away from this class, which may very well come back to bite them in the ass *at* their future jobs/research career. Y'all...I ain't ready for this level of responsibility!?! How do I teach these fairly technical things that took me years to pick up while not ruining anyone's life nor end up making it a bird course???

Well, it happened and I tried my best. Based on the course evaluations, the students seemed to have learned something and had fun, so that's all I can hope for from them. Overall, it was one of the most challenging and rewarding experiences. I've always lamented that research does not bare fruit in any reasonable time (and when it does, you already hate it). But teaching does. You can see it after every lecture, and certainly at the end of the course, the impact you've made on these very real human beings.

Here, I share some of my thoughts from that crazy whirlwind of a month, which I actually jotted down during the process. It's roughly divided into 1) designing the course, 2) game time execution, 3) feedback and reception, and 4) my own development as a student/instructor/person.

For the TL;DR, here are some insights that I gathered that you might find helpful for teaching/TAing your own class:
- design the class backwards: start from what you want them to be able to do by the end, and prepare everything else to make that happen.
- you cannot talk for more than 10-15 minutes and hope students will maintain attention, you just can't. Build activities/breaks into a lecture.
- ask students for feedback early and often, especially if you think you don't know what you are doing. They will tell you, and you can at least decide to change accordingly. And if not, give them a reason for it.
- get technical and emotional support: there are people that know more than you, about teaching and about the thing you're teaching. Also, some days you just want to scream into a pillow for no other reason than the fact that you think you've become a robot that does nothing but prepare for and teach this incredibly mundane thing. My people were Simon (my fantastic life-saver of a TA), Joey, Michael, Brad, and Eran (who gave me all his course material for reference), plus folks at the Teaching Center at UCSD (Noel, Erilynn & others), without whom there probably would have been some empty slides and mental breakdowns.

Hopefully you'll find bits of this useful for your own teaching adventures. If not, at least find it entertaining. I shit you not, there was one night I thought to myself, if I broke my ankles jumping off my apartment patio right now, I probably don't have to lecture tomorrow...

### Course Design
If you asked me 6 months ago about how I would go about designing and teaching a class, I would've said to do it like how I've always taken classes: lecture them on things they needed to learn, make homework assignments to consolidate that knowledge, and make tests to evaluate their learning. Not that that's wrong, but it's actually really hard to approach teaching from that direction. There's an infinite number of ways to cover the topics over the course of 20 lectures, and even more ways to place relative emphasis. Fortunately, to teach as a graduate student, I had to take a college-teaching course myself, and some more training seminars as a part of the SGTS program. This is one of those things that you roll your eyes and begrudgingly oblige at the time because you are required to. It wasn't because I think I was too good for it. Not at all. I was just busy doing research and plugging various holes in my life the months before, like every other PhD student, and the prospect of teaching 5 months later was just a vague notion that didn't require immediate attention.

Well, like most things that's good for me, I realized that it was a huge blessing that I had to do it after the fact. I'll talk about the program specifically in a later section, but one of the most useful concepts I learned was "learning outcome"-driven course design. This is the kind of shit that sounds really obvious when you hear it (most insightful things are), but it's hard to see how I would have spontaneously stumbled upon this framework, much less have enough courage to deviate from what I've always experienced myself to implement it, had I thought this was not encouraged.

The concept is straightforward: you picture what you want the students to be able to accomplish at the end of the class, and design lectures and other material to bring the students towards that goal.

Mind blown, right?

The homework and tests are then to reinforce and evaluate their understanding of the material, for the sole purpose of **your students** reaching those objectives. With that in mind, I just had to think about what I would want the students to be able to do in neural signal processing after 5 weeks, and that was easy:

- I want them to carry out an analysis-driven research project from beginning to end, kind of like a mini-Master's project or honor's thesis project. In my books, you don't know something until you know how to use it, so I wanted them to use what they learned for something that they personally are interested in.
- I wanted them to be able to evaluate analysis decisions they and previous researchers have made, implement algorithms and those decisions in python, and make inferences based on their analysis. This was the highest level goal of critical thinking, which also motivated reading and evaluating scientific literature.
- Most importantly, I wanted them to have something concrete to show for it, so that they can demonstrate their theoretical and practical knowledge to grad schools or future employers. This was my engineering roots, and very much in line with the real-world Data Science philosophy that Brad and Tom had set up for the various courses here at UCSD.

Basically, I wanted them to be able to do the skeletons of everything I can do now, just in a less polished way. Thinking about my own journey, Chris Aimone gave me a shot to stumble through all of this stuff 6 years ago at InteraXon (Muse), and that hands-on experience was more valuable than any class I took before or after by far. So I wanted to replicate that for my students, and in a way that would make them care about what they were doing, more than just getting a good grade.

Hence, the entire focus of this class is to arrive at the end product that is a set of skills the students are able to use, which is demonstrated in the final project to mimic some analyses (that I was personally familiar with) in brain signal processing. If a final project showed technical competence, I was satisfied with their learning. Easy.

It was clear then that assignments are the way to lead them to that goal, helping them to be familiar with the various algorithms in a practical way. They are like the building blocks the students can then take and build different pipelines with. The lectures, labs, and in-class discussions are just me communicating the concepts to them in words, all to help them understand the math and neurophysiology in a theoretical and intuitive way.

With these requirements in mind, I sketched out the major building blocks in the form of python assignments, and designed the syllabus to give them bite-sized chunks towards accomplishing the final goal. I also gave them this roadmap and the expectations in the first class, and referred to it at the beginning of every single lecture. Everyone knows that the mid-quarter or mid-semester slump is a **real struggle**, so I thought having a visible reminder of the very concrete steps they're taking towards the final goal would be motivating. I don't know how much this helped the students, but it certainly helped me get through some days ("thank god we're half-way through").

![roadmap]()

As an aside, I knew I wanted to publish my assignments as stand-alone tutorials, inspired by what Tom and Brad did for the CogSci python ([COGS18][cogs18]) and advanced data science ([COGS108][cogs108]) classes. It stemmed one part from a self-serving motivation to advertise myself for the future, and one part doing what I've always wanted to do anyway, which was to write up these more intuitive but hands-on tutorials (like the Hilbert one from a previous [blog post][hilbert_tut]). My students were the unsuspecting beneficiaries of this decision, since the assignments being self-contained meant that I had to do a lot more hand-holding, walking them through step by step to arrive at the final product.

Well, I cheated a little. What I actually did was to write the assignment as if I was writing a tutorial for my blog, building up the code snippet by snippet, and then just removing parts of it for them to fill in to make it an "assignment". That made life easier too, because I didn't then have to go and solve them myself before grading. My personal favorite is definitely [Assignment 2][A2] for the discrete Fourier transform, because I found the complex dot product idea much easier to grasp than wrestling with integrals for the continuous Fourier transform. Also I did those integrals like 5 years ago and it would be a lot more hassle for not much practical gain, which is exactly what I told the students, and then recommended them to take a DSP class from the ECE department if they want to pursue any of the math formally (which one should).

With all that, I had the syllabus finalized by T-minus 2 weeks, from which point I started preparing for lectures and writing up the assignments. The excitement was building, but so was the stress.

[cogs18][https://cogs18.github.io/intro/]
[cogs108][https://github.com/COGS108/Overview]
[A2][https://github.com/rdgao/COGS118C/blob/master/Assignments/A2-FourierTransform.ipynb]
[hilbert_tut][]

### Execution

`Everyone has a plan until they get punched in the mouth.`

Before the first day of class, I had just about the first week's material all prepared. That was my safety padding, which I thought I'd eat away bit by bit as the term progressed. To no one's surprise, I ate way faster than I had planned to. By the middle of the second week, I was making lectures the day before. Teaching a 1.5 hour lecture 4 days a week, it turns out, is really, really fucking hard. It's not hard like how research is hard, because I know exactly what I had to do to prepare the slides. It's not often that I get to thank past-Richard for something he did, but fully working out the syllabus and the topics I'd cover every lecture made me very appreciative of him (and of the SGTS program).

Teaching 4 days a week was hard because I was not doing or thinking about *anything* else. There were days I would literally wake up, prep, shove some food into my mouth, take the bus to school (and do more prep on the bus), give the lecture (and stick around for lab/discussion twice a week), go to the office to start prepping for next lecture, eat, go home, more prep, sleep. Rinse and repeat. The only thing I did to stay sane was to do some kind of exercise every day, be it lifting, playing ball, or surfing.

The weekends were not much better, as I had to finalize the assignments or midterms (or both), and also tried to do as much as I can to prep and give myself a breather for the following week. Aside from this one Sunday night where I binged half a season of Stranger Things (only because we had a midterm the next day), I think I was at peak efficiency **and** hours worked in a way I haven't been since I bought a phone that can go on the internet. I don't know if I was over-preparing, I certainly felt under-prepared on some days, but it seems to be a common saying that "teaching prep will take as much time as you give it", and for the most part, it was true. It's just that trying to avoid looking like a complete idiot in front of 30 people everyday is such a strong motivator that nothing else really came close, including all the research I wanted to get done.

In the first two weeks, some days felt like I was in an episode of 24, literally racing against time to have enough slides to fill the lecture. As the term progressed, I got a better sense of how much time I needed to finish a lecture that met my own bare minimum standards, and so I was not as stressed about it. Not stressed sometimes just meant pushing the envelope even more, and there were a few days where I finished up slides literally as I was setting up the projector before lecture. Look, I'm not proud of it either, but that's the real shit.

Prepping was only one aspect of the challenge though. I've TA-ed for 5 years now, having led discussion sections for classes ranging from 3 to 40 people. I've also given my fair share of research talks. So as a whole, talking in front of a small room of people does not give me crippling anxiety anymore, thankfully. In fact, I like preparing and giving talks, it was like crafting and telling a story to a live audience, and I always enjoyed making people laugh in unexpected ways. That being said, lecturing for an hour and half is **exhausting**, especially when I'm doing the mental calculus on the fly about how to portion time so we stay on track. And I'm not even talking the whole time, because that's another thing that makes no sense if you think about it for two seconds: you wouldn't watch a movie or a musical where some guy is just **talking at you** for 90 minutes and just assume that you're gonna pay attention, why the hell is that the norm in college? I mean, I get it, and I went through college that way and learned a few things, so it sorta works. But at the same time, it could be so much more.

So I guess the philosophy I tried to embody is, if you don't learn anything, at least be entertained. That probably would've worked out poorly had it not for all the different types of classroom activities I had learned about in the course for college teaching and at SGTS. The bare minimum thing you could do is just to pose a question and have the students talk in groups for a few minutes, which I frequently employed, if for no other reason than for them to get a break from my voice for a second. I can write a whole thing about just my anecdotal experiences of students learning better when they work things out for themselves in 5 minutes, compared to when somebody tells it to them in 30 seconds. It's certainly true for myself.

[questions]
[buzz]

Other strategies include building in "non-thinking" material, like video demonstrations, animations, or even jokes and memes. I don't know if there is solid scientific research showing that those kinds of things promote learning, but they certainly promote keeping myself (the instructor) entertained enough to make it through the lecture without headbanging the wall, so I'm all for it. The students do seem to enjoy it. For the sampling & digitization lecture, I found a [blog post][downsampling] that showed the effect of downsampling music from 16-bit to 8-bit to 4-bit, etc. I played the 4-bit version, and it sounded mangled AF already, so I was like "okay you guys get the point of this right?" I've never seen a class that was so united about anything, where they all screamed "PLAY THE 2-BIT SONG!!!"

Another thing I did, almost purely for everyone's entertainment, was to put up a silly (and somewhat philosophical) question at the beginning of the class that somehow relates to that day's material. We'll talk about it before class, I'll poll their responses, and at some point during the lecture they will realize how the material answered that dumb question at the beginning, and there will be a few chuckles. I just found that this was a much more natural way of transitioning into the start of class, and it provided the same structure everyday (along with reviewing our progress on the roadmap) that it formed a habit. It was same-same but different everyday, and got all of us into rhythm.

So yeah, for the most part, the lectures went well I think. There were definitely parts I wanted to improve on, though. As much as I hate straight lecturing, I had to resort to that for the physiology lecture (L2), because I didn't really know how to make that stuff *fun*. I mean, it's certainly interesting to me that the effect of synaptic currents depends on the membrane potential of the neuron, but that doesn't really land when the students have little to no context in the first place. I just hated myself after that lecture, and vowed to never do it that way again. Another thing I consistently got feedback on was that the slides are not very helpful for studying, because I try to make my lecture slides with as little text as possible, much like my talk slides. The gain in clarity outweighs any potential for missing information in the second case because who really is going to look at your slides after a talk, let's be real. But that's not true in the first case, where students are used to reviewing lecture slides afterwards to consolidate material. This is especially true if they didn't take detailed notes. I tried to mitigate this by giving them study guides for the midterms, and the assignments are self-contained enough that you don't really even need the lecture notes (at least in my opinion), but some students are just more comfortable with stuff on the lecture slides, and I get that.


[downsampling][https://medium.com/@harmonia.global/digital-audio-the-real-meaning-of-8-bit-music-1be5fc8ab2b1]

### Feedback & Reception
A lot of the things that went well for the course, I can't really take credit for, because I picked it up more or less directly from other people and from the SGTS program. The one thing I pat myself on the back for is the abundance of opportunities I provided them for feedback (though this was also a point of emphasis in STGS). From the very first day of lecture, I told them this was my first time teaching a full class and designing my own curriculum, so I'm also learning on the fly and suggestions/feedback are always welcome. If you read between the lines, that meant I have no idea wtf I'm doing. But I figured, if I'm providing a service to a group of people, and I'm not sure if my vision and implementation met their needs and expectations, I could probably just ask them. So I did.

The fastest form of feedback was questions during lecture, and I tried to make the environment as friendly as possible for questions by taking the time to carefully consider them. Some questions were so good that I just had no answer for, which is something every instructor dreads. But the friendly environment helped myself out because when that happened I just told them I didn't know, which was always a good opportunity to break into an activity and have them find the answer on the internet themselves. The hardest moments were those when I finished explaining something and ask "are there any questions?" or "was there anything that's unclear?", and nobody says a damn thing. In those situations, it's always a toss-up between "jesus this is obvious please move on" and "we have no clue wtf you just tried to say and don't even know what questions to ask". Halfway through the course, a student told me about a thing that his professor Lara Rangel (at UCSD) did for her class, which was to ask students to hold up fingers for how much they think they understood something, 1 being completely lost, 5 being let's move on. I stole that so shamelessly like it was the crown jewels, because it immediately let me know how **everyone** was feeling, and cater the solution accordingly.

I also had a "exit note" at the end of every lecture, another concept I picked up at the Teaching Center. Lectures weren't "mandatory", but there was a good portion of the grades dedicated to just showing up. How I took attendance, though, was that I made them fill out a Google survey at the end of every class. It's always the same tinyURL, I just update the survey date and have the data route to a new spreadsheet everyday. It had the same 3 questions:
- What's one thing you learned from this lecture?
- What's one thing that's confusing about this lecture?
- Anything else you would like for me to know, for me to be more helpful, engaging, or otherwise improve your class experience?

For the most part, it was a routine check-in for them to reflect a little on what didn't make sense, and people will have interesting suggestions or funny little responses. I read these everyday because it kept me motivated to see that, at the end of today's hard work, 30 more people in this world now know about sampling rate or aliasing or whatever. Some of my students were such sweethearts that they filled in responses like this (I didn't make this up I swear):

`You are doing a great job as our instructor :), it was fun having you for SS1`

There were definitely times where the survey responses raised an alarm. For the discrete Fourier transform lecture, I was trying to explain near the end why the wavenumbers/DFT frequencies came at the spacing they did, and I tried to show that visually with dots around the unit circle. These were some of the responses I got for "what's confusing" about that lecture:

`the last part`
`the frequency interval at the end`
`the circle with dots for time step example`
`The circle thing. What is it for?`
`Oscillations and consciousness `

That last one confuses me too, so you and me both, my friend. But seeing such a consistent response for the failure of the circle visualization, I knew I had to go over it again, because it was one of the fundamental building blocks towards the DFT, and the time-frequency tradeoff, and everything one does with frequency analysis. So I dedicated half of the next lecture to re-doing this, and then again a few lectures later. I don't know if they got it eventually, since that stopped coming up as a confusing thing. But now I'm really good at explaining this stupid circle thing for the discrete Fourier transform.

I also had similar surveys at the end of every assignment. Student responses ranged from details about the notebook, like separating the response markdown cell from the question prompt because when you edit your response the formatting of the questions gets all screwed up, to bigger conceptual things that warranted some one-on-one help later.

I also tried to give them feedback as often and as quickly as possible, and I had a literal god-sent angel packed in the shape of Simon (then a Master student at the Salk), who implemented Gradescope for the class and proceeded to grade all assignments and midterms within 3 days of submission. That allowed us to have a quick turnaround on assignments, and more importantly, an updated assessment of where the students were at in a super condensed summer session schedule. I did another weird thing, where immediately after the midterm, I collected the responses and read off the correct answers on the projector. This was relieving or cruel, depending on your perspective, but it definitely consolidated learning and made the tests into a **formative assessment** (that's a word I learned at SGTS) where we all discussed why an answer was right or wrong.

I had a final, more extensive survey at the end of the course, in addition to the UCSD official evals. It was definitely relieving to see the results. I had hoped for a challenging but useful and interesting class, and it looks like that's what they got. Plus the numbers for the recommendation rubs the ego a little (a lot). I'm putting these feedback here because, make no mistake, I am proud of this bridge that I built as we crossed the river together. But also I'll probably have to write a teaching statement at some point in the future and I'm just gonna forward this blog post because I'm lazy.



### Final thoughts & the College-Teaching + SGTS Program
It made me think a lot about my role as an instructor. At the college level, plus Google, people are smart enough to find most of the stuff

---


### Preamble & Summary

### Thought Process for Setting up

- group discussions serve as self-teaching, as well as for those that are more skilled to help those that are less skilled
- making a shit ton of slides with the same elements over and over again. Hotkeys ftw http://bermancreative.com/blog/2017/custom-keyboard-commands-for-keynote#teach-me-how-to-keyboard-shortcut
- I’m actually having a lot of fun making the material, but this is super time consuming and hella stressful as the start date looms...

### Lectures: Preparation & Delivery
- finished lecture after an hour…for a 1.5 hour lecture lol. Good thing its just intro stuff today
- talking physiology for 1.5 hours is crazy long. Also not sure how much stuff I’m communicating, could’ve condensed into like 40 minutes probably. Really gotta think about what are the key topics
- My slide style is not great for class room lectures because there aren’t words, so students can’t really study from it later on. Probably need to add a little more text to them.
- build in dead time for fun shit is kinda important, for a 80 min class, just to get a breather in there. "PLAY THE TWO BIT VERSION!"
- evening: second day in a row where i barely got slides done before lecture, again, firm belief that i can get it done now and having the rhythm and confidence means im less stressed about it now, but definitely don’t want to live like this lol. i feel like this is one of those things
- breaking the lecture in the middle kinda got them off track for the second part of the lecture, or maybe i was just really unclear lol idk
- good lectures have a rhythm, for an 80 min lecture, a switch every 10-15 min is good. lecturing for any more than that is very taxing for the students, they have to be asked to do something every 10-15 min
- Lucas told me a thing that Lara does that sounds super useful, which is to ask them to hold up how many fingers for how much they understand the thing that just came out of my mouth
- just finished the last lecture today, man I can’t believe I actually taught a whole college class. WTF? One thing I I learned is that I definitely need extensive preparation. The lectures where I just show up and not having gone through the slides once is terrible.
- Talking for an hour straight is cannot be a sustainable way to teach a class, it just drains the soul from everyone. I have no idea how I learned anything from college by doing that.

### Assignments
- A0 was way too easy for most people I think, though there are a few people that kinda struggled with the more basic stuff, so there might be a bimodal split soon. But A1 will be a lot more of a deeper dive so it should be harder.
- coding as a way to teach math is kinda interesting, because the steps can be decomposed much easier and students can just try and rerun code while experimenting, with immediate feedback, while math problems is not necessarily the case, unless intermediate steps were given

### Student Feedback
- the daily feedback form is already super valuable
- most of the time, students ask questions that i did not make clear on in lecture. there are only a few instances where somebody asks a questions that clearly does not demonstrate having thought about it, but for the most part, i think im personally responsible for the lack of (100%, at least) clarity
- lots more questions on Piazza about not understanding something. Reading over the lab feedback, there were specific points that individual students were confused about, and the lab demonstrated that to themselves, even though they were able to finish it. But not many people came to office hours to check in.
- As much as I don’t like midterms, students are just not quite motivated to study and clear up their confusion without a midterm.
- I prep my material assuming a single template of students, but student background and where they’re at are so varied, especially as we get to the later stages of class. this variance kinda naturally occurred, as much as i tried to prevent it, so probably have to think about how to cater to the different segments
- along the same vein, not everyone wants an A for the class, and you never know what their expectation is. So I think for me, the bare minimum is to make it interesting enough to them so that they will pursue it
- i forget that social hierarchy is still a thing in undergrad
- Just gave the second midterm, they were way less happy about this than MT1. Lots of discussions right after it was done, I think there was a large degree of uncertainty, rather than anyone actually screwing it up. As a whole, it tested for more conceptual applications than hard math, which I thought would be easier. But now I feel like I may not have prepared them well enough? All in all though, I think it was a fair test, and they more or less agreed, though I think it depends on expectation. A few people gunning for 100 and falling short will complain a lot more than people rightly getting an 80, which is what I was shooting for, especially with the gimme questions and the review beforehand.
- **Examples of feedback form and response***
download the project comments

### My Own Learning
- reviewing FTs for lecture tomorrow, really starting to learn all the details yet again, which is really great
- i need to do things that i care about more, otherwise this is way too draining and it doesnt motivate me at all, its as if im TAing. here, i have the freedom to teach whatever material however i want, though i definitely want to be responsible and leave them with everything they need to know
-

### Learning Curve, Stress & Confidence
- Shaky on some explanations (like backprop)
- okay i think i’m getting into form, finding a rhythm. today’s lecture (sampling) ventured into more technical things, but the discussions worked well and went over by only 10 min, so i’m getting a sense of how to structure things
- I feel like this is the closest I’ve been to having a breakdown, there’s just so much shit to take care off all the time. And it’s not so much the class itself, that I’m getting the hang of now, but everything else I’ve neglected that’s piling up because of the class, people waiting on me for shit, etc. Probably not a healthy approach to go ALL IN but I feel a certain responsibility to teach the students well
- to every pre-tenure professor i’ve taken a class with, i’m sorry and deeply sympathize
- doing the example made me SWEAT, and the lecture in general was just all over the place. not great
- some people asked for more rigorous math proofs, which is nice, but also i feel that it exposes what i dont know.
- I feel like I really messed up on explaining Nyquist frequency in lecture, and never really got back to it properly
- I get hella stressed about covering all the necessary material, the stuff i know and think are important, but they literally have no clue. like i can waltz in and talk about half the material, as long as it covers the time, it’s fine. this is a trip
- im basically working 12 hours a day on the days i teach, which is insane, but i get to not think about anything else and just focus, and it makes me believe that i can do pretty much anything when 1) i have the incentive to, 2) i have to get it done
- I’m not sure if I feel like an imposter or a fraud. Sometimes I feel like I should be giving more effort to the class, or just be better prepared in general, especially when I explained something wrong or poorly, or didn’t have enough time to cover the material I wanted to. At the end of the day, I have a set of things in mind that I think they should know, and I can obviously make the tests and assignments as easy or hard as I want, but what it comes down to is whether they can use what they learned in the real world
- I got the claps at the end, and it was great!

### SGTS
* on SGTS: This is an extremely valuable program considering how academia actively de-emphasis teaching for research, especially for graduate students. Having a group of people that values teaching and trains you to be as prepared as possible for it is an essential part of becoming an academic, and should be prioritized even more in light of how undervalued GOOD teaching is. Even though some of the material felt like common sense at times, I would have been insanely overwhelmed without the structure provided by the program, as well as being connected to peers all going through this at the same time. Just going through this experience knowing that there's somebody there to help you and empathize with you was very comforting, even if you don't end up using a lot of the resources. Having the weekly conversations and an observation also made sure I was on track, otherwise I can easily see how a course can spiral out of control in the extremely tight summer scheduling. Having gone through this as a graduate student, I'm a lot more confident in my ability to do it as a career if it came to that.
* Thanks to everyone for making this happen and helping us along every step of the way, really couldn't have done it without the SGTS program! I don't have any feedback that's generally applicable for everyone, I think the tweaks I would make are specific to my own course and issues that came up. As a whole, the program (including the intro college teaching course) was organized well, and the essentials absolutely necessary for everyone were covered (outcomes, syllabus, etc.) These were very valuable and delivered at appropriate times.
* For my class, I had a lot of opportunities for student feedback, so in retrospect, I would have wanted more guidance and resources for effectively gathering and using student feedback along the course of the session. But there are a million of these things that the program can prepare for and I don't think frontloading all of them before the session starts is necessarily the right way to go. People are a lot more receptive to instructions and training in general when they see how it applies to a problem they have/might have.
* Maybe one general-level feedback is that SGTS can implement hard deadlines for certain milestones, like the syllabus and various assignments. Obviously people are busy during the quarter immediately before, and are going to be unhappy about yet another thing to do, but I can't imagine anyone being anything but grateful after the fact. Especially seeing how SGTS is a selective program, I don't think it's unreasonable to have deadlines for the privilege of being in the program. I was so glad to have gotten my syllabus done (sorta) early, setting up a structure for the course which I was just able to follow, it would've been great if I had done the same for the assignments. In general, that would reduce the stress for during the session, but I think that too is just part of the experience.
* Thanks again for everything. This was an insane and valuable experience and I'm really grateful for all the help from SGTS and the teaching hub.



- hard but learned something / good evals
- structured note taking breaks to reorganize thoughts: lecture style + not being down with slides
- download course evals

what i learned:
- best way to learn is through teaching because: 1) you don't want to look like an idiot so you really need to know it well, 2) you have to find ways of explaining something from multiple (simple) perspectives
- committing the resource

what i'd do differently:
- incorporate more material that I'm less familiar with
- upload slides beforehand with exercise/fill in the blank
