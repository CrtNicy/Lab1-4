# Work 5: Responsive Design

## Overview
Creating responsive and mobile-friendly web layouts.

## Key Features
- Responsive design principles
- Mobile-first approach
- Cross-browser compatibility
- Media queries

## Technologies
- CSS Grid
- Flexbox
- Media Queries
- Mobile Optimization

## Code Examples

### Responsive Grid Layout
```css
/* Mobile First Grid Layout */
.container {
    display: grid;
    grid-template-columns: 1fr;
    gap: 1rem;
    padding: 1rem;
}

/* Tablet Layout */
@media screen and (min-width: 768px) {
    .container {
        grid-template-columns: repeat(2, 1fr);
    }
}

/* Desktop Layout */
@media screen and (min-width: 1024px) {
    .container {
        grid-template-columns: repeat(3, 1fr);
        max-width: 1200px;
        margin: 0 auto;
    }
}
```

### Flexbox Navigation
```css
/* Mobile Navigation */
.nav {
    display: flex;
    flex-direction: column;
    padding: 1rem;
}

.nav-list {
    display: none; /* Hidden by default on mobile */
    flex-direction: column;
    gap: 1rem;
}

.nav-list.active {
    display: flex;
}

.nav-toggle {
    display: block; /* Show hamburger menu on mobile */
}

/* Desktop Navigation */
@media screen and (min-width: 768px) {
    .nav {
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
    }

    .nav-list {
        display: flex;
        flex-direction: row;
        gap: 2rem;
    }

    .nav-toggle {
        display: none; /* Hide hamburger menu on desktop */
    }
}
```

### Responsive Images
```css
/* Responsive Images */
.responsive-image {
    max-width: 100%;
    height: auto;
}

.image-gallery {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1rem;
    padding: 1rem;
}

/* Image Card */
.image-card {
    position: relative;
    overflow: hidden;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.image-card img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.3s ease;
}

.image-card:hover img {
    transform: scale(1.05);
}

/* Responsive Typography */
html {
    font-size: 16px;
}

@media screen and (min-width: 768px) {
    html {
        font-size: 18px;
    }
}

@media screen and (min-width: 1200px) {
    html {
        font-size: 20px;
    }
} 