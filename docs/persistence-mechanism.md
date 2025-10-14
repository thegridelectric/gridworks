# Distributed SCADA Persistence Mechanism

## Overview
TBD ADD DIAGRAM

## Architecture Components

### gridworks-uploader
- Repository: https://github.com/SmoothStoneComputing/gridworks-uploader
- Role: Local buffering and reliable upstream delivery
- [Details...]

### gridworks-ingester  
- Repository: https://github.com/thegridelectric/gridworks-ingester
- Role: Cloud-based persistence to PostgreSQL and S3
- [Details...]

### gridworks-proactor
- Repository: https://github.com/SmoothStoneComputing/gridworks-proactor
- Role: Foundation for reliable actor-based message delivery
- [Details...]

## Message Flow
[Your flow diagram]

## Credits
Architecture designed by Andrew Schweitzer (Smooth Stone Computing)