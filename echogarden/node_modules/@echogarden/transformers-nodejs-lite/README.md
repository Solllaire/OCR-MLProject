# Transformers for Echogarden

This package is a highly reduced fork of the [Xenova JavaScript port of 🤗 transformers](https://github.com/xenova/transformers.js). It's modified for the particular needs of Echogarden, to ensure very small package and dependency sizes.

It **keeps**:
* Models
* Tokenizers
* Node.js port (only `onnxruntime-node` is supported, as a peer dependency)

It **removes**:
* All pipelines
* All processors
* All image and audio utilities
* Web port (`onnxruntime-web` dependency is removed)
* Documentation
* Tests
* Examples
