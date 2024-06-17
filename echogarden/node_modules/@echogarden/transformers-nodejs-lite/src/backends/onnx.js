import * as ONNX_NODE from 'onnxruntime-node'

/** @type {any} The ONNX runtime module. */
export const ONNX = ONNX_NODE.default

export const executionProviders = [
    'cpu'
]

export const logSeverityLevel = 3
