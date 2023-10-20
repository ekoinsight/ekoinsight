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

## Project summary

### The issue we are hoping to solve

While formal education about recycling at school is great, cementing this education into daily habits for children requires something a little more dynamic and engaging. Drawing inspiration from the popular tamagotchi game, our app seeks to foster a sense of responsibility towards the environment by encouraging users to take care of their miniature planet-like pet to learn about sustainable practices.

### How our technology solution can help

Interactive AI backed Tamagotchi-style app helping foster eco-responsibility and nurturing.

### Our idea

Many of us remember the hit pet caring simulation called Tamagotchi. This simple gadget grabbed the attention of a generation of children who were all thinking about how to take care of their pets on a daily basis. We aim to transfer that same devotion and attention but towards taking care of a digital pet planet earth. 

While on the surface the fun comes from feeding and caring for a cute digital pet, on a deeper level we're looking to help keep sustainability at the top of their minds by having them continuously look for recyclable objects to feed their pets and having educational content in return in the form of their pet's reactions. 

Furthermore, instilling a habit of thinking about recycling has its benefits. Research reveals that students adhering to pro-environmental behaviors tend to be more actively involved in recycling. (https://www.mdpi.com/2673-4060/2/3/21). 

Aiming for this age group is also ideal since early childhood education is particularly influential in shaping attitudes and values, making it a critical period for instilling sustainable practices (https://amshq.org/Blog/2023-05-24-Reduce-Reuse-Recycle-Environmental-Education-in-the-Montessori-Classroom).

The creature is brought to life with textual communications using Watson X and the Llama 2 model, customizable in look (coming soon) and fed by children uploading pictures of recyclable objects from their the real world surroundings. 

With the Blip2 model, we have the capability to discern the contents of an image and relay this data to the LLM. The LLM then processes this information, generating a score and providing an educational response for the creature to compose in return. Currently, this feature is available exclusively in English for our MVP1 version. However, we are in the final stages of development to include support for multiple languages, aiming to ensure our app's accessibility to a diverse global audience.

When an item is deemed recyclable, the creature's well-being is bolstered, leading to a joyful response and the delivery of educational insights about the item. Notably, the creature's physical appearance also undergoes dynamic changes. Conversely, if an item is non-recyclable, the creature's health deteriorates, resulting in a more somber response.

Our plan encompasses an expansion of user interaction options, ranging from engaging in full-fledged conversations with the creature to receiving push notifications that remind users when the tiny pet planet is in need of sustenance.

It's worth acknowledging the evolving nature of AI and image recognition. Enhancing and updating the creature's performance and capabilities can be accomplished seamlessly through a simple API switch.

As a side note, our team underwent a recent shift in our concept, and as a result, our repository and domain name may still display our previous name, "ekoinsight."


## Technology implementation

### IBM AI service(s) used

Utilizing the Llama 2 foundation model, the Watson X system employs prompts to interact with it. It employs Python Langchain to communicate with the underlying Llama 2 base model. The primary purpose of this interaction is to inquire about the sustainability of an item and receive a response imbued with a specific personality. This functionality is triggered by invoking the ApiWatsonX class in the "backend/ekoinsight/app.py" module.

### Other IBM technology used

Our infrastructure provisioning relies on the IBM virtual private cloud using the service  'Virtual Server for VPC.' We maintain two distinct machines for distinct purposes: one dedicated to development and the other serving as the host for user-facing infrastructure. Each of these machines is equipped with a configuration featuring 4 vCPUs and 16 GiB of memory.

To enable routing to our virtual private cloud, we employ the "Floating IP for VPC" service. Through this service, we have allocated two user-accessible IP addresses for our VPC machines.


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

