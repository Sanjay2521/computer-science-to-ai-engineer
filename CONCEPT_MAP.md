# CONCEPT MAP

How concepts depend on one another. Arrows mean *"is a prerequisite for / enables."* This is a
living document — expand it as you learn. `→` = leads to; indentation = sub-dependencies.

## The digital-hardware spine
```
transistors
 → logic gates (AND, OR, NOT, NAND, NOR, XOR)
   → combinational circuits
     → adders, multiplexers, decoders
   → sequential circuits
     → flip-flops → registers → counters
       → ALU + control unit
         → CPU
           → machine instructions (ISA)
             → assembly
               → fetch–decode–execute cycle
                 → interrupts, I/O, buses
                   → operating systems
                     → programming languages
```

## The number & encoding thread
```
binary → hexadecimal → unsigned integers → two's complement (signed)
       → floating point (IEEE 754)
       → character encodings (ASCII, Unicode/UTF-8)
boolean algebra → logic gates (connects into the hardware spine)
```

## The memory & data thread
```
memory (addresses, bytes)
 → arrays
   → strings
   → data structures (lists, stacks, queues, hash tables, trees, graphs, heaps, tries)
     → algorithms (search, sort, traversal, DP, greedy, graph algorithms)
       → databases (tables, indexes/B-trees, query planning, transactions)
         → data engineering (pipelines, warehouses, columnar formats)
     → model tensors (n-dim arrays → NumPy → PyTorch)
```

## The mathematics → AI thread
```
linear algebra
 → vectors → dot products → matrices → matrix multiplication
   → linear transformations → basis/dimension → eigen-intuition
     → embeddings
       → similarity / semantic search
         → attention (Q·K scores) → multi-head attention
           → transformers → LLMs

calculus
 → limits → derivatives → partial derivatives → gradients → chain rule
   → optimization → gradient descent
     → backpropagation → training neural networks

probability & statistics
 → random variables → distributions → expectation/variance
   → Bayes → inference
     → loss functions → evaluation metrics
       → machine learning → model monitoring / drift

information theory
 → entropy → cross-entropy → KL divergence
   → classification losses → LLM training objectives
```

## The systems → networking → agents thread
```
operating systems
 → processes → threads → scheduling → permissions
   → sandboxes / containers / VMs
     → computer-use agents (safe execution environments)

networking (layers, TCP/IP)
 → HTTP/HTTPS/TLS
   → REST APIs
     → tool calling (LLM invokes functions over schemas)
       → MCP (client ↔ server protocol for tools/resources)
         → AI agents (loop: plan → tool → observe → act)
           → browser agents (DOM/accessibility tree + automation)
           → coding agents (repo index + patch + test loop)
```

## The ML → production thread
```
statistics → machine learning → deep learning → transformers → LLMs
 → RAG (retrieval-grounded generation)
   → AI engineering (structured output, guardrails, tracing, cost)
     → MLOps/LLMOps (serving, monitoring, drift, evaluation)
       → security & responsible AI (injection, least privilege, audit)
         → AI research (reproduce, ablate, report)
```

## Cross-layer connections worth remembering
- **Floating point** (hardware) explains **numerical instability** in training (DL).
- **Cache/memory hierarchy** (hardware) explains **batching & data loaders** (DL perf).
- **Hash tables** (DSA) underlie **tokenizer vocabularies** and **vector index buckets**.
- **Matrix multiplication** (math) *is* the forward pass of a linear layer and attention.
- **HTTP + auth** (networking) *is* the transport for **model APIs** and **MCP**.
- **OS permissions/sandboxes** *are* the safety boundary for **computer-use agents**.
- **Transactions/idempotency** (DB/distributed) *are* how **agents retry safely**.

> As you complete each phase, add the new concepts and the surprising connections you
> discover here. The connections are where real understanding lives.
