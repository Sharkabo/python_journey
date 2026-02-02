# Side Projects Roadmap - FastAPI Backend Developer

## Overview

This roadmap outlines the side projects you should build to demonstrate your skills and land a Python backend job in Taiwan. Each project builds on previous knowledge and showcases different aspects of backend development.

**Total Projects**: 6 projects (3 essential + 3 advanced)
**Timeline**: 4-6 months (alongside learning)
**Goal**: Build a portfolio that impresses employers and demonstrates production-ready skills

---

## Project Progression Strategy

### Phase Distribution
- **After PHASE_1**: 1 foundational project
- **After PHASE_3**: 2 core API projects
- **After PHASE_5**: 3 advanced projects (including 1 AI-powered)

### Portfolio Goals
1. Demonstrate FastAPI proficiency
2. Show database design skills
3. Prove deployment capability
4. Include AI integration (high-demand skill in Taiwan)
5. Show testing and documentation quality

---

## Essential Projects (Must Build)

### Project 1: Task Management API
**Timeline**: After PHASE_1 (2 weeks)
**Complexity**: Beginner
**Tech Stack**: Python, FastAPI basics, SQLite, Git

**Features**:
- User authentication (JWT)
- CRUD operations for tasks
- Task categories and tags
- Due dates and priorities
- RESTful API design

**Learning Objectives**:
- Practice OOP from PHASE_1
- Apply type hints in real project
- Understand basic API structure
- Version control with Git

**Portfolio Value**:
- Shows you can build a complete API
- Demonstrates CRUD mastery
- Clean, well-documented code

**README Requirements**:
- API documentation with examples
- Setup instructions
- Example requests/responses
- Database schema diagram

---

### Project 2: E-commerce Product API
**Timeline**: After PHASE_3 (3-4 weeks)
**Complexity**: Intermediate
**Tech Stack**: FastAPI, PostgreSQL, SQLAlchemy, Redis, Docker

**Features**:
- Product catalog with categories
- Shopping cart functionality
- Order management
- Inventory tracking
- Search and filtering
- Redis caching for popular products
- JWT authentication with roles (admin/customer)

**Learning Objectives**:
- Complex database relationships
- Caching strategies
- Performance optimization
- API security best practices
- Docker containerization

**Portfolio Value**:
- Real-world applicable project
- Shows understanding of scalability
- Demonstrates security awareness
- Production-ready architecture

**README Requirements**:
- Complete API documentation (Swagger auto-generated)
- Database schema with relationships
- Architecture diagram
- Performance benchmarks
- Docker setup instructions

---

### Project 3: Social Media API with AI Features
**Timeline**: After PHASE_5 (4-5 weeks)
**Complexity**: Advanced
**Tech Stack**: FastAPI, PostgreSQL, Redis, Celery, OpenAI API, Docker, GCP Cloud Run

**Features**:
- User profiles and authentication
- Post creation with image upload
- Follow/unfollow system
- Feed algorithm (simple)
- AI-powered content moderation (OpenAI)
- AI-powered post suggestions
- Real-time notifications (WebSockets)
- Background tasks with Celery
- Rate limiting

**Learning Objectives**:
- Microservices patterns
- AI API integration
- Asynchronous tasks
- WebSocket implementation
- Cloud deployment

**Portfolio Value**:
- Shows AI integration (highly valued in Taiwan 2025-2026)
- Complex feature set
- Production deployment experience
- Modern tech stack

**README Requirements**:
- Comprehensive API documentation
- System architecture diagram
- AI integration explanation
- Deployment guide
- Live demo link (GCP Cloud Run)

---

## Advanced Projects (Optional but Highly Recommended)

### Project 4: Real-time Chat API
**Timeline**: After PHASE_5 (3 weeks)
**Complexity**: Intermediate-Advanced
**Tech Stack**: FastAPI, WebSockets, Redis Pub/Sub, PostgreSQL

**Features**:
- Real-time messaging
- Group chats and DMs
- Online status indicators
- Message history
- Typing indicators

**Why Build This**:
- WebSocket expertise is rare and valuable
- Shows real-time system understanding
- Redis Pub/Sub knowledge

---

### Project 5: Multi-tenant SaaS API
**Timeline**: After PHASE_5 (4 weeks)
**Complexity**: Advanced
**Tech Stack**: FastAPI, PostgreSQL (row-level security), Stripe API, Docker

**Features**:
- Multi-tenant architecture
- Subscription management with Stripe
- Usage-based billing
- Tenant isolation
- Admin dashboard API

**Why Build This**:
- SaaS experience is highly valued
- Payment integration skills
- Complex data isolation patterns

---

### Project 6: AI-Powered Code Review Bot
**Timeline**: After PHASE_5 (3-4 weeks)
**Complexity**: Advanced
**Tech Stack**: FastAPI, OpenAI API, GitHub API, Celery, PostgreSQL

**Features**:
- GitHub webhook integration
- Automated code review with AI
- Pull request comments
- Code quality metrics
- Learning from accepted reviews

**Why Build This**:
- Combines AI + DevOps
- GitHub integration experience
- Webhook handling skills
- Very impressive portfolio piece

---

## Project Quality Standards

### Each Project Must Have

**Code Quality**:
- Type hints throughout
- Comprehensive tests (pytest)
- 70%+ code coverage
- Linting (ruff/black)
- No security vulnerabilities

**Documentation**:
- Clear README with setup instructions
- API documentation (Swagger UI)
- Architecture diagrams
- Database schema diagrams
- Environment setup guide

**Deployment**:
- Docker containerization
- At least one project deployed live (GCP Cloud Run recommended)
- CI/CD pipeline (GitHub Actions)

**Git Practices**:
- Meaningful commit messages
- Feature branches
- Pull request workflow
- Clean commit history

---

## Timeline and Priorities

### Months 1-2 (Alongside PHASE_1)
- **Goal**: Build Project 1 (Task Management API)
- Focus on OOP and clean code
- Practice Git workflow

### Months 3-5 (Alongside PHASE_2-3)
- **Goal**: Build Project 2 (E-commerce API)
- Focus on database design
- Implement caching
- Deploy to cloud

### Months 6-8 (Alongside PHASE_4-5)
- **Goal**: Build Project 3 (Social Media + AI)
- Focus on AI integration
- Implement real-time features
- Production deployment

### Months 9+ (While job hunting)
- **Optional**: Build Projects 4-6 based on interest
- Contribute to open source
- Write technical blog posts about your projects

---

## Making Your Projects Stand Out

### For Taiwan Market Specifically

1. **Add Traditional Chinese Support**
   - Internationalization (i18n)
   - Chinese error messages
   - Shows local market awareness

2. **Include Popular Taiwan Services**
   - Line Login integration
   - ECPay payment gateway
   - Taiwan address validation

3. **Documentation in Both Languages**
   - README in English
   - API docs in Traditional Chinese
   - Shows communication skills

4. **Local Deployment Options**
   - GCP Taiwan region
   - Mention compliance (GDPR, Taiwan privacy laws)

---

## GitHub Best Practices

### Repository Structure
```
project-name/
├── .github/
│   └── workflows/
│       └── ci.yml
├── app/
│   ├── api/
│   ├── models/
│   ├── schemas/
│   └── services/
├── tests/
├── docs/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── README.md
└── .env.example
```

### README Template
```markdown
# Project Name

Brief description (1-2 sentences)

## Features
- Feature 1
- Feature 2

## Tech Stack
- FastAPI
- PostgreSQL
- etc.

## Live Demo
[Link to deployed app]

## Setup
1. Clone repo
2. Install dependencies
3. Run migrations
4. Start server

## API Documentation
[Link to Swagger UI]

## Architecture
[Diagram or explanation]

## Testing
```bash
pytest
```

## License
MIT
```

---

## Portfolio Presentation

### Your GitHub Profile Should Show
1. **6 pinned repositories**: Your best projects
2. **Consistent commits**: Regular activity
3. **Quality over quantity**: Better to have 3 excellent projects than 10 mediocre ones
4. **Professional profile**:
   - Photo
   - Bio highlighting "FastAPI Backend Developer"
   - Location: Taiwan
   - Link to deployed projects

### When Applying for Jobs

**Resume Projects Section**:
```
E-commerce Product API | FastAPI, PostgreSQL, Redis, Docker
- Built RESTful API serving 1000+ requests/min with Redis caching
- Implemented JWT authentication and role-based access control
- Deployed to GCP Cloud Run with CI/CD pipeline
- [GitHub] [Live Demo]
```

**Interview Talking Points**:
- Why you chose this architecture
- Challenges you faced and how you solved them
- What you'd do differently now
- Performance optimizations you implemented

---

## Success Metrics

### You're Ready to Apply When You Have

**Minimum Requirements**:
- 3 complete projects (Projects 1-3)
- At least 1 deployed live
- All with comprehensive README
- Tests with 70%+ coverage

**Competitive Portfolio**:
- 4-5 projects
- 2+ deployed live
- 1 with AI integration
- Active GitHub contributions
- Technical blog posts

**Outstanding Portfolio**:
- All 6 projects
- All deployed with custom domains
- AI-powered features
- Open source contributions
- Published npm/PyPI package
- Technical speaking/blogs

---

## Resources for Building

### Design Inspiration
- GitHub Explore (trending FastAPI projects)
- Dev.to FastAPI articles
- Real companies' tech blogs

### When You Get Stuck
1. Check FastAPI documentation
2. Search Stack Overflow
3. Ask in Python Taiwan community
4. Review course material (PHASE_GUIDE.md)

### Deployment Resources
- GCP free tier (enough for demos)
- Railway.app (easy deployment)
- Render.com (free tier)

---

## Final Advice

**Quality > Quantity**:
Build fewer projects, but make them excellent. One deployed, well-documented, AI-powered project is worth more than five incomplete ones.

**Show Your Work**:
- Document your decision-making
- Explain trade-offs in README
- Include performance metrics
- Show before/after optimization results

**Make It Yours**:
- Add unique features
- Solve a real problem you've encountered
- Customize the UX/DX
- Innovation impresses employers

**Keep Learning**:
- Each project should teach you something new
- Refactor old projects as you learn more
- Update projects with new skills

---

**Remember**: Your goal is not just to build projects, but to build a portfolio that demonstrates you can contribute to a professional team from day one. Focus on quality, documentation, and deployed projects that employers can actually use and evaluate.

Good luck building!
