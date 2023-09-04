[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
    <img src="logo.png" alt="logo" width="300">
    <br/>
    <small><i>A static URL shortener runs on Github Page</i></small>
    <br/>
</p>


## What is this?

A static URL shortener runs on Github Page.

## How does it work?

1. Clone this repo
2. Config URLS in `config.json`. Syntax below
3. Run `python main.py`, the relevant HTML files will be generated
4. Push & deploy to [Github Page](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)
5. User access a HTML file, get redirected to the desired URL using `<meta http-equiv="refresh" />`

**Config file structure**

```json
{
  "urls": {
    "path1": "https://example.com",
    "path2": "https://example.com/path2",
    "parent-path": {
      "child1": "https://example.com/1",
      "child2": "https://example.com/2"
    }
  }
}
```

This will result in the following mappings:
```
https://<github user name>.github.io/<repo name>/path1              --> https://example.com
https://<github user name>.github.io/<repo name>/path2              --> https://example.com/path2
https://<github user name>.github.io/<repo name>/parent-path/child1 --> https://example.com/1
https://<github user name>.github.io/<repo name>/parent-path/child2 --> https://example.com/2

```


<!-- LICENSE -->
## License

Distributed under the MIT License.

<!-- CONTRIBUTING -->
## Contributing

Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/dthung1602/r.svg?style=flat-square
[contributors-url]: https://github.com/dthung1602/r/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/dthung1602/r.svg?style=flat-square
[forks-url]: https://github.com/dthung1602/r/network/members
[stars-shield]: https://img.shields.io/github/stars/dthung1602/r.svg?style=flat-square
[stars-url]: https://github.com/dthung1602/r/stargazers
[issues-shield]: https://img.shields.io/github/issues/dthung1602/r.svg?style=flat-square
[issues-url]: https://github.com/dthung1602/r/issues
[license-shield]: https://img.shields.io/github/license/dthung1602/r.svg?style=flat-square
[license-url]: https://github.com/dthung1602/r/blob/master/LICENSE
