<div id="top"></div>
.
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/ErikBavenstrand/Advent-of-Code">
    <img src="images/AoC.jpg" alt="Logo">
  </a>

<hr/>

</div>

<!-- ABOUT THE PROJECT -->

## About

Solutions to (some) Advent of Code challenges written in `Python`

### Requirements

- `Python 3.10`
- `Pipenv`

### Running

First generate the boilerplate code:

```
$ python aoc.py [year] [day] generate --author "Firstname Lastname"
```

Implement the solutions for part A and B and add the test case to `./[year]/[day]/testcase.txt` (needs to be manually copeid from AoC website).

To test the solutions run:

```
$ python aoc.py [year] [day] test
```

Finally, run the following command to solve and submit using the real data.

**Important**: follow the instructions [here](https://github.com/wimglenn/advent-of-code-data#quickstart) on how to add your AoC session cookie to your local machine.

```
$ python aoc.py [year] [day] solve --submit
```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/ErikBavenstrand/Advent-of-Code.svg?style=for-the-badge
[contributors-url]: https://github.com/ErikBavenstrand/Advent-of-Code/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ErikBavenstrand/Advent-of-Code.svg?style=for-the-badge
[forks-url]: https://github.com/ErikBavenstrand/Advent-of-Code/network/members
[stars-shield]: https://img.shields.io/github/stars/ErikBavenstrand/Advent-of-Code.svg?style=for-the-badge
[stars-url]: https://github.com/ErikBavenstrand/Advent-of-Code/stargazers
[issues-shield]: https://img.shields.io/github/issues/ErikBavenstrand/Advent-of-Code.svg?style=for-the-badge
[issues-url]: https://github.com/ErikBavenstrand/Advent-of-Code/issues
[license-shield]: https://img.shields.io/github/license/ErikBavenstrand/Advent-of-Code.svg?style=for-the-badge
[license-url]: https://github.com/ErikBavenstrand/Advent-of-Code/blob/master/LICENSE.txt
