# Conway's Game of Life

Terminal implementation of Conway's cellular automaton with color visualization and configuration options.

## Demo
<img width="1083" height="1429" alt="screenshot_1" src="https://github.com/user-attachments/assets/2caf5ee0-ee07-4d58-b700-48dbbaf0b2ff" />
<img width="747" height="254" alt="screenshot_2" src="https://github.com/user-attachments/assets/085f5cb2-c6a2-49b4-b6ae-60b50149e728" />
![gameoflifegif](https://github.com/user-attachments/assets/9c0eb989-07de-488f-8c05-61035dc8a260)

## What it does

Grid of cells, each alive or dead. Every generation, cells check their 8 neighbors and update according to Conway's rules:

- Live cell with 0-1 neighbors dies (underpopulation)
- Live cell with 2-3 neighbors lives 
- Live cell with 4+ neighbors dies (overpopulation)
- Dead cell with exactly 3 neighbors becomes alive

**Random revival**: Optional 2% chance for dead cells to revive each step. Prevents complete extinction.

**Configurable**: Field size (40-120x20-60), speed (0.05-0.5s delay), revival toggle.

## Usage

```bash
python main.py
