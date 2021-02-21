# dcm2bids
Your friendly DICOM converter.

[![Documentation](https://img.shields.io/badge/Documentation-dcm2bids-succes.svg)](https://unfmontreal.github.io/Dcm2Bids)
[![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.2616548.svg)](https://zenodo.org/badge/latestdoi/59581295)
[![Anaconda-Server Badge](https://anaconda.org/conda-forge/dcm2bids/badges/latest_release_date.svg)](https://anaconda.org/conda-forge/dcm2bids)


[![](https://github.com/unfmontreal/Dcm2Bids/workflows/Tests/badge.svg)](https://github.com/unfmontreal/Dcm2Bids/actionsk)
[![](https://codecov.io/gh/unfmontreal/Dcm2Bids/branch/master/graph/badge.svg)](https://codecov.io/gh/unfmontreal/Dcm2Bids)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


[![PyPI version](https://img.shields.io/pypi/v/dcm2bids)](https://pypi.org/project/dcm2bids)
[![Anaconda-Server Badge](https://anaconda.org/conda-forge/dcm2bids/badges/version.svg)](https://anaconda.org/conda-forge/dcm2bids)
[![Docker container](https://badgen.net/docker/pulls/unfmontreal/dcm2bids?icon=docker&label=pulls)](https://hub.docker.com/r/unfmontreal/dcm2bids)


[![](https://img.shields.io/pypi/l/dcm2bids)](/docs/LICENSE.txt)

---

`dcm2bids` reorganises NIfTI files using [dcm2niix][dcm2niix-github] into the [Brain Imaging Data Structure][bids] (BIDS).

## Scope

`dcm2bids` is a community-centered project. It aims to be a friendly,
easy-to-use tool to convert your dicoms. Our main goal is to make the dicom
to BIDS conversion as effortless as possible. Even if in the near future
more advanced features will be added, we'll keep the focus on your day
to day use case without complicating anything. That's the promise of the `dcm2bids` project.

## Documentation

Please take a look at the [documentation][dcm2bids-doc] to:

* [Learn about bids][bids-spec] with some dataset [examples][bids-examples]
* [Install dcm2niix][dcm2niix-install]
* [Install dcm2bids][dcm2bids-install]
* [Follow the tutorial][dcm2bids-tutorial]
* [Seek for more advanced usage][dcm2bids-advanced]

## Issues

We work hard to make sure `dcm2bids` is robust and we welcome comments and questions to make sure it meets your use case! Here's our preferred workflow:

- If you have a usage question, please post your issue on Neurostars with `dcm2bids` as an optional tag. The tag is really important because Neurostars will only notify us if the tag is present.

- If you think you've found a bug, please open an issue here. To do this, you'll need a GitHub account. See our [contributing guide][dcm2bids-contributing] for more details.


[bids]: http://bids.neuroimaging.io/
[bids-examples]: https://github.com/bids-standard/bids-examples
[bids-spec]: https://bids-specification.readthedocs.io/en/stable/
[dcm2bids-doc]: https://unfmontreal.github.io/Dcm2Bids
[dcm2bids-install]: https://unfmontreal.github.io/Dcm2Bids/#install
[dcm2bids-tutorial]: https://unfmontreal.github.io/Dcm2Bids/tutorial
[dcm2bids-advanced]: https://unfmontreal.github.io/Dcm2Bids/advance/
[dcm2bids-issues]: https://github.com/UNFmontreal/Dcm2Bids/issues
[dcm2niix-install]: https://github.com/rordenlab/dcm2niix#install
[dcm2niix-github]: https://github.com/rordenlab/dcm2niix
[neurostars]: https://neurostars.org/
[dcm2bids-contributing]: https://unfmontreal.github.io/Dcm2Bids/CONTRIBUTING.md