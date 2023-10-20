# Setup notes for backend:

Install deps with pip install -r requirements

python3.11 -m spacy download en_core_web_sm

wget https://huggingface.co/spaces/abhishek/StableSAM/resolve/main/sam_vit_h_4b8939.pth

mkdir models
mv sam_vit_h_4b8939.pth models

cd ekoinsight/backend/ekoinsight

Start with python app.py 

# IBM template below


[![License](https://img.shields.io/badge/License-Apache2-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0) [![Community](https://img.shields.io/badge/Join-Community-blue)](https://developer.ibm.com/callforcode/solutions/projects/get-started/)

_INSTRUCTIONS: This GitHub repository serves as a template you can use to create a new project for the [2023 Call for Code Global Challenge](https://developer.ibm.com/callforcode/global-challenge/). Use the **Use this template** button to create a new version of this repository and start entering content for your own Call for Code submission project. Make sure you have [registered for the 2023 Call for Code Global Challenge](https://developer.ibm.com/callforcode/global-challenge/register/) to access resources and full project submission instructions. Remove any "INSTRUCTIONS" sections when you are ready to submit your project._

_New to Git and GitHub? This free online course will get you up to speed quickly: [Getting Started with Git and GitHub](https://www.coursera.org/learn/getting-started-with-git-and-github)_.

# PlanetPalz (previously known as ekoinsight)

- [Project summary](#project-summary)
  - [The issue we are hoping to solve](#the-issue-we-are-hoping-to-solve)
  - [How our technology solution can help](#how-our-technology-solution-can-help)
  - [Our idea](#our-idea)
- [Technology implementation](#technology-implementation)
  - [IBM AI service(s) used](#ibm-ai-services-used)
  - [Other IBM technology used](#other-ibm-technology-used)
  - [Solution architecture](#solution-architecture)
- [Presentation materials](#presentation-materials)
  - [Solution demo video](#solution-demo-video)
  - [Project development roadmap](#project-development-roadmap)
- [Additional details](#additional-details)
  - [How to run the project](#how-to-run-the-project)
  - [Live demo](#live-demo)
- [About this template](#about-this-template)
  - [Contributing](#contributing)
  - [Versioning](#versioning)
  - [Authors](#authors)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

_INSTRUCTIONS: Complete all required deliverable sections below._

## Project summary

### The issue we are hoping to solve

While formal education about recycling at school is great, cementing this education into daily habits for children requires something a little more dynamic and engaging. Drawing inspiration from the popular tamagotchi game, our app seeks to foster a sense of responsibility towards the environment by encouraging users to take care of their miniature planet-like pet to learn about sustainable practices.

### How our technology solution can help

Interactive AI backed Tamagotchi-style app helping foster eco-responsibility and nurturing.

### Our idea

Many of us remember the hit pet caring simulation called Tamagotchi. This simple gadget grabbed the attention of a generation of children who were all thinking about how to take care of their pets on a daily basis. We aim to transfer that same devotion and attention but towards taking care of a digital pet planet earth. 

While on the surface the fun comes from feeding and caring for a cute digital pet, on a deeper level we're looking to help keep sustainability at the top of their minds by having them continuously look for recyclable objects to feed their pets and having educational content in return in the form of their pet's reactions. 

And instilling a habit of thinking about recycling has its benefits. Research reveals that students adhering to pro-environmental behaviors tend to be more actively involved in recycling. (https://www.mdpi.com/2673-4060/2/3/21). 

Aiming for this age group is also ideal since early childhood education is particularly influential in shaping attitudes and values, making it a critical period for instilling sustainable practices (https://amshq.org/Blog/2023-05-24-Reduce-Reuse-Recycle-Environmental-Education-in-the-Montessori-Classroom).

The creature will be brought to life with textual communications using Watson X and the Llama 2 model, customizable in look and fed via pictures of recyclable objects children can identify in the real world. 
Using the Blip2 model we identify what's in the picture and pass that information along to the LLM which converts that into a score and an educational response for the creature to write back. At the moment it's only in English due to lack of time but we are very close to allow a response in any language.

If the item is recyclable, the creature's health pool increases, and the creature responds in a happy manner with educational information regarding the item. If the item is not recyclable, then its health pool decreases and the creature responds in kind.  

We intend to have more ways for the user to interact with the creation including full on conversations and push notifications to remind the user whenever the tiny pet planet is hungry.

The AI and image recognition space is continuously improving and updating the creatures' performance and abilities would only be an api switch away.

One thing of note (Up until a very recent pivot in idea, our team was called ekoinsight, so our repo and domain name will show the old name)


## Technology implementation

### IBM AI service(s) used

_INSTRUCTIONS: Included here is a list of commonly used IBM AI services. Remove any services you did not use, or add others from the linked catalog not already listed here. Leave only those included in your solution code. Provide details on where and how you used each IBM AI service to help judges review your implementation. Remove these instructions._

Watson X prompting using Llama 2 foundation model
Querying the base model Llama 2 via python langchain to ask how sustainable a item given is and to reply back with a certain personality.
(backend/ekoinsight/app.py calls the ApiWatsonX class)

### Other IBM technology used

INSTRUCTIONS: List any other IBM technology used in your solution and describe how each component was used. If you can provide links to/details on exactly where these were used in your code, that would help the judges review your submission.

### Solution architecture

Diagram and step-by-step description of the flow of our solution:

![Video transcription/translaftion app](https://developer.ibm.com/developer/tutorials/cfc-starter-kit-speech-to-text-app-example/images/cfc-covid19-remote-education-diagram-2.png)

1. The user navigates to the site and uploads a video file.
2. Watson Speech to Text processes the audio and extracts the text.
3. Watson Translation (optionally) can translate the text to the desired language.
4. The app stores the translated text as a document within Object Storage.

## Presentation materials

_INSTRUCTIONS: The following deliverables should be officially posted to your My Team > Submissions section of the [Call for Code Global Challenge resources site](https://cfc-prod.skillsnetwork.site/), but you can also include them here for completeness. Replace the examples seen here with your own deliverable links._

### Solution demo video

https://www.youtube.com/watch?v=IoCffN-gAz8&ab_channel=AK_RD44

### Project development roadmap

The project currently does the following things.

- Engages children to feed and take care of their pet earth creature, thus forming a habit of thinking about sustainability.
- The user can send it pictures of recyclable material they see in real life, which is a novel way of tying
- The earth pet educates the child based on whatever the child just fed it. 

In the future we plan to...

See below for our proposed schedule on next steps after Call for Code 2023 submission.

![Roadmap](./images/roadmap.jpg)

## Additional details

_INSTRUCTIONS: The following deliverables are suggested, but **optional**. Additional details like this can help the judges better review your solution. Remove any sections you are not using._

### How to run the project

INSTRUCTIONS: In this section you add the instructions to run your project on your local machine for development and testing purposes. You can also add instructions on how to deploy the project in production.

### Live demo

You can find a running system to test at...

See our [description document](./docs/DESCRIPTION.md) for log in credentials.

---

_INSTRUCTIONS: You can remove the below section from your specific project README._

## About this template

### Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

### Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

### Authors

<a href="https://github.com/Call-for-Code/Project-Sample/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=Call-for-Code/Project-Sample" />
</a>

- **Billie Thompson** - _Initial work_ - [PurpleBooth](https://github.com/PurpleBooth)

### License

This project is licensed under the Apache 2 License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments

- Based on [Billie Thompson's README template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2).

