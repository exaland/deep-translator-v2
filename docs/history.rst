==================
Important History
==================

- 1.11.4

  - Fixed ``ChatGptTranslator`` on standard installations by calling the OpenAI
    Chat Completions API through the existing ``requests`` dependency.
  - Replaced the default ``gpt-3.5-turbo`` model with ``gpt-6-luna``.
    The ``model`` argument still lets callers select a compatible model.
  - Read ``OPENAI_API_KEY`` when creating a translator and retained support
    for the legacy ``OPEN_API_KEY`` variable.
  - Renamed the PyPI distribution to ``deep-translator-v2`` under
    Exaland Concept. The ``deep_translator`` import and existing CLI commands
    remain compatible.
  - Aligned the distribution's license metadata with the existing Apache 2.0
    license.

- 1.5.4 @kuspia: restructured google trans url to resolve language conflicts. Supercedes fix in 1.5.3
- 1.5.3 bug fix to resolve translation issues with russian-ukranian languages
- 1.5.0 improved cli functionality with streamlined commands and numerous bugfixes.
- 1.4.4 added support for papago, added opt params, fixed deepl free api
- 1.4.3 added support deepl free api
- 1.4.2 added proxy support
- 1.3.4 bug fixes for the dutch language
- 1.3.3 fixed bug in google translate

- 1.2.5: added support for the DeeplTranslator translator
- 1.2.4: added support for the QcriTranslator translator
- 1.2.1: added support for the yandex translator
- 1.1.9: fixed bug in requests
- 1.1.5: added language detection
- 1.1.3: added support for mymemory
- 1.0.4: added support for pons
- 1.0.2: added support for linguee
- 1.0.0: added support for google translate
