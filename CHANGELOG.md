# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.2] - 2023-11-12
### Added
- Better explanation of codes.
- This CHANGELOG file to hopefully help track this project's progress.
- An feature to update Sagemode.
### Changed
- Spinner for rich's status.
- Made the Notify class as a helper class instead of inheriting from it.
- Methods of Notify class from instance methods to a static methods.
- Rely on rich library instead of the color() function from accessories module that
  has been removed.
### Fixed
- Error pretty printing the banner in windows command prompt.
### Removed
- color() function in accessories module.

## [1.1.3] - 2023-11-18
### Added
- User-Agents list in sites.py to avoid being blocked by the servers
- A way to output the status code in notify.not_found() method.
- More sites and more error checkings for false positives.
### Fixed
- Soft 404 errors (reduced false positive responses of sites)
