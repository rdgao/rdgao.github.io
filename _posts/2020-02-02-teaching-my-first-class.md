---
title: 'This Shit was Hard: Thoughts from Teaching My First College Course [4/52]'
tags: [General Science, Data & Technology]
status: publish
type: post
published: True
header:
  overlay_image: /assets/images/blog/2020-02-02-roadmap.png
  overlay_filter: rgba(0,0,0,0.7)
  teaser: /assets/images/blog/2020-02-02-roadmap.png
classes:
  - wide
permalink: /blog/:year/:month/:day/

excerpt: "I used to think there are professors that gave a shit, and those who don't. I think that's still largely true, but I realized that just giving a shit, while a prerequisite, is not enough to make you a good teacher. Because it's hard. And like anything, there is a lot of knowledge about how to do it well that you might never learn, because you would've never thought to ask."
---

As noted elsewhere on this website, I am very poor at forecasting how I will feel about something in the future. That's how I stumbled into teaching an actual freaking college class this past summer.

Earlier 2019, there was an opportunity to apply for this fellowship(?) at UCSD called [Summer Graduate Teaching Scholars (SGTS)][sgts], where they pay you a little extra money and give you a lot of training to teach your own course here. I thought, if there's any chance of me becoming a professional academic someday, maybe I should see how I like teaching an actual class, instead of just basing my experiences on being teaching assistants. Considering the extra money and the (__very necessary__) training, I was sold. What I clearly didn't consider in the sale was the absolute pandemonium that my summer 2019 would become as a result.

This is the story of how I ended up teaching my own course for the first time ever, on [Neural Signal Processing][repo].

This experience was up there for "hardest things I've ever done", in many ways. For one, I haven't consistently worked this many hours a week since the first two years of undergrad in Engineering Science. It was a rollercoaster ride that made 5 weeks seem like 5 months at times, but now that it's over, it felt like an instant. The harder part was coming to grips with the fact that 1) I have control over 33 people's grade for a senior-level class, which may have a real impact on their future job prospects, and 2) I have control over the technical content they walked away with from this class, which may very well come back to bite them in the ass __at__ their future jobs/research career. Y'all. I'm not ready for this level of responsibility!?! How do I teach these fairly technical things that took me years to pick up while not ruining anyone's life nor end up making it a breezy course?

Well, it happened and I tried my best. Based on the course evaluations, the students seemed to have learned something and had fun, so that's all I can hope for from them. Overall, it was one of the most challenging and rewarding experiences. I've always lamented that research does not bare fruit in any reasonable time (and when it does, you already hate it). But teaching does. You can see it after every lecture, and certainly at the end of the course, the impact you've made on these very real human beings. I'm not usually one to brag, but this message after the class ended really made those crazy days worth it:

![][review]
---
Here, I share some of my thoughts from that crazy whirlwind of a month, which I mostly jotted down during the process. It's roughly divided into 1) designing the course, 2) game time execution, 3) feedback & future improvements, and 4) my own development as a student/instructor/person. You might want to read parts 1-3 if you ever want to teach your own class, otherwise, skip to part 4 for pure reflective entertainment.

For the TL;DR, here are some insights that I gathered that you might find helpful for teaching/TAing your own class:
- design the class backwards: start from what you want them to be able to do by the end, and prepare everything else to make that happen.
- you cannot talk for more than 10-15 minutes and hope students will maintain attention. You just can't. Build activities/breaks into a lecture.
- ask students for feedback early and often, especially if you think you don't know what you are doing. They will tell you, and you can at least decide to change accordingly. And if not, give them a reason for it.
- get technical and emotional support: there are people that know more than you, about teaching and about the thing you're teaching. Also, some days you just want to scream into a pillow for no other reason than the fact that you think you've become a robot that does nothing but prepare for and teach this incredibly mundane thing. My people were Simon (my fantastic life-saver of a TA), Joey, Michael, Brad, and Eran (who very kindly gave me all his course material for reference), plus folks at the Teaching Center at UCSD (Noel, Erilynn & others), without whom there probably would have been some empty slides and mental breakdowns.

Hopefully you'll find bits of this useful for your own teaching adventures. If not, at least find it entertaining. I shit you not, there was one night I thought to myself, if I broke my ankles jumping off my apartment patio right now, I probably don't have to lecture tomorrow...

---
# I. Course Design
If you asked me 12 months ago about how I would go about designing and teaching a class, I would've said to do it like how I've always taken classes: lecture them on things they needed to learn, make homework assignments to consolidate that knowledge, and make tests to evaluate their learning. Not that that's wrong, but it's actually really hard to approach teaching from that direction. There's an infinite number of ways to cover the topics over the course of 20 lectures, and even more ways to place relative emphasis. Fortunately, to teach as a graduate student, I had to take a college-teaching course myself, and some more training seminars as a part of the SGTS program. This is one of those things that you roll your eyes and begrudgingly oblige at the time because you are required to. It wasn't because I think I was too good for it. Not at all. I was just busy doing research and plugging various holes in my life the months before, like every other PhD student, and the prospect of teaching 5 months later was just a vague notion that didn't require immediate attention.

Well, like most things that's good for me, I realized after the fact that it was a huge blessing. The benefits of the program are sprinkled in various sections, but one of the most useful concepts I learned was "learning outcome"-driven course design. This is the kind of shit that sounds really obvious when you hear it (most insightful things are), but it's hard to see how I would have spontaneously stumbled upon this framework, much less have enough courage to deviate from what I've always experienced myself to implement it, had I thought this was not encouraged.

The concept is straightforward: you picture what you want the students to be able to accomplish at the end of the class, and design lectures and other material to bring the students towards that goal.

Mind blown, right?

The homework and tests are then to reinforce and evaluate their understanding of the material, for the sole purpose of **your students** reaching those objectives. With that in mind, __I just had to think about what I would want the students to be able to do in neural signal processing after 5 weeks, and that was easy:__

- I want them to carry out an analysis-driven research project from beginning to end, kind of like a mini-Master's project or honor's thesis project. In my books, you don't know something until you know how to use it, so I wanted them to use what they learned for something that they personally are interested in.
- I wanted them to be able to evaluate analysis decisions they and previous researchers have made, implement algorithms and those decisions in python, and make inferences based on their analysis. This was the highest level goal of critical thinking, which also motivated reading and evaluating scientific literature.
- Most importantly, I wanted them to have something concrete to show for it, so that they can demonstrate their theoretical and practical knowledge to grad schools or future employers. This was my engineering roots, and very much in line with the real-world Data Science philosophy that Brad had set up for the various courses here at UCSD.

Basically, I wanted them to be able to do the skeletons of everything I can do now, just in a less polished way. Thinking about my own journey, Chris Aimone gave me a shot to stumble through all of this stuff 8 years ago (_holy shit_) at InteraXon, and that hands-on experience was more valuable than any class I took before or after by far. So I wanted to replicate that for my students, and in a way that would make them care about what they were doing, more than just getting a good grade. Hence, the entire focus of this class is to arrive at the end product that is a set of skills the students are able to use, which is demonstrated in the final project to mimic some analyses (that I was personally familiar with) in brain signal processing. If a final project showed technical competence, I was satisfied with their learning. Easy.

It was clear then that assignments are the way to lead them to that goal, helping them to be familiar with the various algorithms in a practical way. They are like the building blocks the students can then take and build different pipelines with. The lectures, labs, and in-class discussions are just me communicating the concepts to them in words, all to help them understand the math and neurophysiology in a theoretical and intuitive way.

With these requirements in mind, I sketched out the major building blocks in the form of python assignments, and designed the syllabus to give them bite-sized chunks towards accomplishing the final goal. I also gave them this roadmap and the expectations in the first class, and referred to it at the beginning of every single lecture. Everyone knows that the mid-quarter or mid-semester slump is a **real struggle**, so I thought having a visible reminder of the very concrete steps they're taking towards the final goal would be motivating. I don't know how much this helped the students, but it certainly helped me get through some days ("thank god we're half-way through").

![][roadmap]

As an aside, I knew I wanted to publish my assignments as stand-alone tutorials, inspired by what [Tom][tom] did for the CogSci python ([COGS18][cogs18]) and advanced data science ([COGS108][cogs108]) classes. It stemmed one part from a self-serving motivation to advertise myself for the future, and one part doing what I've always wanted to do anyway, which was to write up these more intuitive but hands-on tutorials (like the Hilbert one from a previous [blog post][hilbert_tut]). My students were the unsuspecting beneficiaries of this decision, since the assignments being self-contained meant that I had to do a lot more hand-holding, walking them through step by step to arrive at the final product.

Well, I cheated a little. What I actually did was to write the assignment as if I was writing a tutorial for my blog, building up the code snippet by snippet, and then just removing parts of it for them to fill in to make it an "assignment". That made life easier too, because I didn't then have to go and solve them myself before grading. My personal favorite is definitely [Assignment 2][A2] for the discrete Fourier transform, because I found the complex dot product idea much easier to grasp than wrestling with integrals for the continuous Fourier transform. Also I did those integrals like 5 years ago and it would be a lot more hassle for not much practical gain, which is exactly what I told the students, and then recommended them to take a DSP class from the ECE department if they want to pursue any of the math formally (which one should).

With all that, I had the syllabus finalized by T-minus 2 weeks, from which point I started preparing for lectures and writing up the assignments. The excitement was building, but so was the stress.

---
> Everyone has a plan until they get punched in the mouth.

# II. Execution
Before the first day of class, I had just about the first week's material all prepared. That was my safety padding, which I thought I'd eat away bit by bit as the term progressed. To no one's surprise, I ate way faster than I had planned to. By the middle of the second week, I was making lectures the day before. Teaching a 1.5 hour lecture 4 days a week, it turns out, is really, really fucking hard. It's not hard like how research is hard, because I know exactly what I had to do to prepare the slides. It's not often that I get to thank past-Richard for something he did, but fully working out the syllabus and the topics I'd cover every lecture made me very appreciative of him (and of the SGTS program).

Teaching 4 days a week was hard because I was not doing or thinking about *anything* else. There were days I would literally wake up, prep, shove some food into my mouth, take the bus to school (and do more prep on the bus), give the lecture (and stick around for lab/discussion twice a week), go to the office to start prepping for next lecture, eat, go home, more prep, sleep. Rinse and repeat. The only thing I did to stay sane was to do some kind of exercise every day, be it lifting, playing ball, or surfing.

The weekends were not much better, as I had to finalize the assignments or midterms (or both), and also tried to do as much as I can to prep and give myself a breather for the following week. Aside from this one Sunday night where I binged half a season of Stranger Things (only because we had a midterm the next day), I think I was at peak efficiency **and** hours worked in a way I haven't been since I bought a phone that can go on the internet. I don't know if I was over-preparing, I certainly felt under-prepared on some days, but it seems to be a common saying that "teaching prep will take as much time as you give it", and for the most part, it was true. It's just that trying to avoid looking like a complete idiot in front of 30 people everyday is such a strong motivator that nothing else really came close, including all the research I wanted to get done.

In the first two weeks, some days felt like I was in an episode of 24, literally racing against time to have enough slides to fill the lecture. As the term progressed, I got a better sense of how much time I needed to finish a lecture that met my own bare minimum standards, and so I was not as stressed about it. Not stressed sometimes just meant pushing the envelope even more, and there were a few days where I finished up slides literally as I was setting up the projector before lecture.

Look, I'm not proud of it either, but that's the real shit.

Prepping was only one aspect of the challenge though. I've TA-ed for 5 years now, having led discussion sections for classes ranging from 3 to 40 people. I've also given my fair share of research talks. So as a whole, talking in front of a small room of people does not give me crippling anxiety anymore, thankfully. In fact, I like preparing and giving talks, it was like crafting and telling a story to a live audience, and I always enjoyed making people laugh in unexpected ways. That being said, lecturing for an hour and half is **exhausting**, especially when I'm doing the mental calculus on the fly about how to portion time so we stay on track. And I'm not even talking the whole time, because that's another thing that makes no sense if you think about it for two seconds: you wouldn't watch a movie or a musical where some guy is just **talking at you** for 90 minutes and just assume that you're gonna pay attention, why the hell is that the norm in college? I mean, I get it, and I went through college that way and learned a few things, so it sorta works. But at the same time, it could be so much more.

So I guess the philosophy I tried to embody is, if you don't learn anything, at least be entertained. That probably would've worked out poorly had it not for all the different types of classroom activities I had learned about in the course for college teaching and at SGTS. The bare minimum thing you could do is just to pose a question and have the students talk in groups for a few minutes, which I frequently employed, if for no other reason than for them to get a break from my voice for a second. I can write a whole thing about just my anecdotal experiences of students learning better when they work things out for themselves in 5 minutes, compared to when somebody tells it to them in 30 seconds. It's certainly true for myself.

![][funslides]

Other strategies include building in "non-thinking" material, like video demonstrations, animations, or even jokes and memes. I don't know if there is solid scientific research showing that those kinds of things promote learning, but they certainly promote keeping myself (the instructor) entertained enough to make it through the lecture without headbanging the wall, so I'm all for it. The students do seem to enjoy it. For the sampling & digitization lecture, I found a [blog post][downsampling] that showed the effect of downsampling music from 16-bit to 8-bit to 4-bit, etc. I played the 4-bit version, and it sounded mangled AF already, so I was like "okay you guys get the point of this right?" I've never seen a class that was so united about anything, where they all screamed "PLAY THE 2-BIT SONG!!!"

Another thing I did, almost purely for everyone's entertainment, was to put up a silly (and somewhat philosophical) question at the beginning of the class that somehow relates to that day's material. We'll talk about it before class, I'll poll their responses, and at some point during the lecture they will realize how the material answered that dumb question at the beginning, and there will be a few chuckles. I just found that this was a much more natural way of transitioning into the start of class, and it provided the same structure everyday (along with reviewing our progress on the roadmap) that it formed a habit. It was same-same but different everyday, and got all of us into rhythm.

So yeah, for the most part, the lectures went well enough. There were definitely parts I wanted to improve on, though. As much as I hate straight lecturing, I had to resort to that for the physiology lecture (L2), because I didn't really know how to make that stuff *fun*. I mean, it's certainly interesting to me that the effect of synaptic currents depends on the membrane potential of the neuron, but that doesn't really land when the students have little to no context in the first place. I just hated myself after that lecture, and vowed to never do it that way again.

Another thing I consistently got feedback on was that the slides are not very helpful for studying, because I try to make my lecture slides with as little text as possible, much like my talk slides. The gain in clarity outweighs any potential for missing information in the second case because who really is going to look at your slides after a talk, let's be real. But that's not true in the first case, where students are used to reviewing lecture slides afterwards to consolidate material. This is especially true if they didn't take detailed notes. I tried to mitigate this by giving them study guides for the midterms, and the assignments are self-contained enough that you don't really even need the lecture notes (at least in my opinion), but some students are just more comfortable with stuff on the lecture slides, and I get that.

---
# III. Feedback & Reception
I can't really take credit for a lot of the things that went well for the course, because I picked it up more or less directly from other people and from the SGTS program. The one thing I pat myself on the back for is the abundance of opportunities I provided them for feedback (though this was also a point of emphasis in SGTS). From the very first day of lecture, I told them this was my first time teaching a full class and designing my own curriculum, so I'm also learning on the fly and suggestions/feedback are always welcome. If you read between the lines, that meant I have no idea wtf I'm doing. But I figured, if I'm providing a service to a group of people, and I'm not sure if my vision and implementation met their needs and expectations, I could probably just ask them. So I did.

The fastest form of feedback was questions during lecture, and I tried to make the environment as friendly as possible for questions by taking the time to carefully consider them. Some questions were so good that I just had no answer for, which is something every instructor dreads. But the friendly environment helped myself out because when that happened I just told them I didn't know, which was always a good opportunity to break into an activity and have them find the answer on the internet themselves. The hardest moments were those when I finished explaining something and ask "are there any questions?" or "was there anything that's unclear?", and nobody says a damn thing. In those situations, it's always a toss-up between "jesus this is obvious please move on" and "we have no clue wtf you just tried to say and don't even know what questions to ask". Halfway through the course, a student told me about a thing that his professor Lara Rangel (at UCSD) did for her class, which was to ask students to hold up fingers for how much they think they understood something, 1 being completely lost, 5 being let's move on. I stole that shamelessly, because it immediately let me know how **everyone** was feeling, and to cater the solution accordingly.

I also had a "exit note" at the end of every lecture, another concept I picked up at the Teaching Center. Lectures weren't "mandatory", but there was a good portion of the grades dedicated to just showing up. How I took attendance, though, was that I made them fill out a Google Forms survey at the end of every class. It's always the same tinyURL, I just update the survey date and have the data route to a new spreadsheet everyday. It had the same 3 questions:
- What's one thing you learned from this lecture?
- What's one thing that's confusing about this lecture?
- Anything else you would like for me to know, for me to be more helpful, engaging, or otherwise improve your class experience?

For the most part, it was a routine check-in for them to reflect a little on what didn't make sense, and people will have interesting suggestions or funny little responses. I read these everyday because it kept me motivated to see that, at the end of today's hard work, 30 more people in this world now know about sampling rate or aliasing or whatever. Some of my students were such sweethearts that they filled in responses like this (I didn't make this up I swear):

`You are doing a great job as our instructor :), it was fun having you for SS1`

There were definitely times where the survey responses raised an alarm. For the discrete Fourier transform lecture, I was trying to explain near the end why the wave-numbers/DFT frequencies came at the spacing they did, and I tried to show that visually with dots around the unit circle. These were some of the responses I got for "what's confusing" about that lecture:

`"the last part"`

`"the frequency interval at the end"`

`"the circle with dots for time step example"`

`"The circle thing. What is it for?"`

`"Oscillations and consciousness"`

That last one confuses me too, so you and me both, my friend.

But seeing such a consistent response for the failure of the circle visualization, I knew I had to go over it again, because it was one of the fundamental building blocks towards the DFT, and the time-frequency tradeoff, and everything one does with frequency analysis. So I dedicated half of the next lecture to re-doing this, and then again a few lectures later. I don't know if they got it eventually, since that stopped coming up as a confusing thing. But now I'm really good at explaining this stupid circle thing for the discrete Fourier transform.

(it was this slide lol)

![][wavenumber]

I also had similar surveys at the end of every assignment. Student responses ranged from details about the notebook, like separating the response markdown cell from the question prompt because when you edit your response the formatting of the questions gets all screwed up, to bigger conceptual things that warranted some one-on-one help later. I also tried to give them feedback as often and as quickly as possible, and I had a literal god-sent angel packed in the shape of Simon Niu (a Master student at the Salk), who implemented Gradescope for the class and proceeded to grade all assignments and midterms within 3 days of submission. That allowed us to have a quick turnaround on assignments, and more importantly, an updated assessment of where the students were at in a super condensed summer session schedule.

__I did another weird thing, where immediately after the midterm, I collected the responses and read off the correct answers on the projector.__ This was kind or cruel, depending on your perspective, but it definitely consolidated learning and made the tests into a **formative assessment** (that's a word I learned at SGTS) where we all discussed why an answer was right or wrong. First midterm, they left the room into a bright and sunny afternoon. Second midterm, I thought somebody was going to egg my car.

I had a final, more extensive survey at the end of the course, in addition to the UCSD official evaluations. It was definitely relieving to see the results. I had hoped for a challenging but useful and interesting class, and it looks like that's what they got. Plus the numbers for the recommendation rubs the ego a little (a lot). I'm putting these feedback here because, make no mistake, I am proud of this bridge that I built as we crossed the river together. __But also I'll probably have to write a teaching statement at some point in the future and I'm just gonna forward this blog post because I'm lazy.__

![][capes]

---
# IV. Final Thoughts, Personal Development & the College-Teaching + SGTS Program
People say that having a baby makes you understand your own parents much more. I think this works for teachers as well. I used to think there are professors that gave a shit, and those who don't. I think that's still largely true, but I realized that just giving a shit, while a prerequisite, is not enough to make you a good teacher. Because it's hard. And like anything, there is a lot of knowledge about how to do it well that you might never learn, because you would've never thought to ask. It's not breaking news that a large portion of academia implicitly devalues teaching, if not explicitly. But I do think there are a lot of well-intending college professors that don't just want to be a research scientist, and actually do value teaching college students, as insane of a job as that is when you have 500+ students in a class. It's just that over time, people might become discouraged or jaded while not seeing their students respond positively, perhaps feeling that the students are struggling with something that they should not be struggling with. Again, I'm usually not one for training seminars, but maybe professors need help too, in this new job that being a graduate student and postdoc never prepared you for.

I can't imagine what I would've done without that college teaching class and the SGTS program. The scarier thing is that I probably wouldn't even know what I was doing that was counterproductive, instead leaving the experience thinking I or my students were subpar. I'm not claiming that I know the ins and outs of teaching a college-level class as a professor just from this one class, not at all. In fact, just the opposite: I think it's ludicrous that people could become college professors just by virtue of having a PhD, an achievement that is as meaningless as being a trivia champion when it comes to teaching and pedagogy. At the same time, it makes me think back to all the college professors I had, some of whom we could all sense were trying, but just couldn't keep the class awake. Teachers are people too, and it's really nice to hear a "you're doing a good job" every now and then.

Along that vein, I don't know if I will ever get to teach again, but having gotten the feedback and encouragement I got, I can certainly say that it will be a meaningful experience next time as well, and there is definitely an opportunity to impact students' lives - however briefly - that is bestowed upon a professor. Like all things, this first class of mine will always be special. Maybe it's because I'm still not completely disconnected from pop culture, or maybe it's because I'm a 12-year old inside, but I could related to many of my students: the quiet ones, the bombastic ones, the overeager ones, the ones that don't give a shit about any of this except their final grade, and the ones with a spark in their eyes and ask good questions but don't quite know how to study effectively. Those are various versions of myself and my friends, and it was wonderful to have their trust for 5 weeks even though I was very candidate about my obvious lack of experience.

One thing that became evident is that, obviously, every student is different. But I designed the class for __a prototypical student__, be that some average person, or a specific instance of a person. Over time, student's performances diverged, either because of differing goals and abilities, or because the course was suboptimal for their learning style. This is a challenge that will be present for as long as we have classes with many more students than instructors, but maybe one way to ameliorate it is to emphasize learning skills, or some kind of meta-learning/self-learning, than to focus on the content itself. Teaching this class made me think a lot about my role as an instructor. At the college level, plus Google, people are smart enough to find most of the stuff on their own, you just need to show them how and point them down a path.

Lastly, the parable is true: nothing is more effective for learning than trying to teach it to someone else. I thought I was familiar with signal processing and Fourier Transforms before this class, boy did we get more intimate after those 5 weeks. There were a few nights where I was making slides and slowly began to panic because I couldn't explain what I had wanted to in a simple way, which of course meant I never really learned it myself. So teaching this class had an unintended side benefit of brushing up my own knowledge. One thing I do regret though is that I wish I had taught more things that were slightly more outside of my own expertise, which I didn't stray too far into in fear of totally bombing the lecture. Everything about this is hard, and the only way to make it "easier" is to teach things that you find interesting, and sometimes that could mean new things that you want to explore as a student yourself.

---

<iframe width="560" height="315" src="https://www.youtube.com/embed/vY48xCKQZks" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

[sgts]:https://undergrad.ucsd.edu/programs/sgts.html
[repo]:https://github.com/rdgao/cogs118c
[roadmap]:/assets/images/blog/2020-02-02-roadmap.png
[review]:/assets/images/blog/2020-02-02-message.png
[tom]:https://twitter.com/Tomdonoghue
[cogs18]:https://cogs18.github.io/intro/
[cogs108]:https://github.com/COGS108/Overview
[A2]:https://github.com/rdgao/COGS118C/blob/master/Assignments/A2-FourierTransform.ipynb
[hilbert_tut]:http://www.rdgao.com/roemerhasit_Hilbert_Transform/
[funslides]:/assets/images/blog/2020-02-02-funslides.png
[downsampling]:https://medium.com/@harmonia.global/digital-audio-the-real-meaning-of-8-bit-music-1be5fc8ab2b1
[capes]:/assets/images/blog/2020-02-02-capes.png
[wavenumber]:/assets/images/blog/2020-02-02-wavnumber.png
