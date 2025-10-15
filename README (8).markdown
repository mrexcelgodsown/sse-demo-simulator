# Secure Service Edge (SSE) Demo Simulator

A demo simulator for Secure Service Edge (SSE) concepts, featuring a distributed task queue for processing security tasks (e.g., DLP scanning). Built with FastAPI, Redis, React, Tailwind CSS, and p5.js for animated visualizations, styled like JetBrains 2020 for a clean, professional look.

## Features
- **Security Task Queuing**: Enqueue data for mock SSE processing (e.g., threat detection, DLP masking of PII).
- **Real-Time Dashboard**: View task status, queue length, and animated scan results with CGI/VFX effects.
- **JetBrains 2020 Design**: JetBrains Mono font, blue accents, minimalistic cards, and smooth hover animations.
- **Authentication**: JWT for secure task submission.
- **Responsive UI**: Adapts to desktop and mobile.

## Demo
Try the dashboard at [https://mrexcelgodsown.github.io/sse-demo-simulator](https://mrexcelgodsown.github.io/sse-demo-simulator).

![Demo GIF](assets/demo.gif)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/mrexcelgodsown/sse-demo-simulator.git
   ```
2. **Backend Setup** (requires Docker):
   ```bash
   docker-compose up -d
   ```
3. **Frontend Setup**:
   - Open `index.html` in a browser for the dashboard (no server needed).
   - Or host on GitHub Pages (see below).

## Usage
1. Open the dashboard (`index.html` or live URL).
2. Click "Login" (username: `admin`, password: `password`) to authenticate.
3. Enter data (e.g., "Credit card: 4111 1111 1111 1111") and click "Enqueue Data".
4. View task status, scan animation (CGI/VFX style), and results (e.g., masked PII).
5. Toggle dark/light theme for a JetBrains-inspired look.

## Tech Stack
- **Backend**: Python (FastAPI), Redis, JWT
- **Frontend**: React, Tailwind CSS, p5.js (animations)
- **Deployment**: Docker, Docker Compose
- **Fonts**: JetBrains Mono

## Architecture
- **API**: FastAPI serves endpoints (`/login`, `/tasks`) with JWT authentication.
- **Queue**: Redis stores tasks and manages the queue (`task_queue` list).
- **Workers**: Python scripts process tasks asynchronously, simulating SSE (e.g., DLP masking).
- **Dashboard**: React frontend fetches job data and displays animated scans with p5.js.

## Future Enhancements
- Add real threat detection using ML (e.g., integrate TensorFlow).
- Implement SD-WAN simulation for routing.
- Support partner integration APIs.

## License
MIT License