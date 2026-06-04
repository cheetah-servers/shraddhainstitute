document.addEventListener('DOMContentLoaded', () => {

// ==========================================
// 1. SCROLL REVEAL EFFECTS
// ==========================================
const revealElements = document.querySelectorAll('.reveal');

if ('IntersectionObserver' in window) {
const revealObserver = new IntersectionObserver((entries) => {
entries.forEach(entry => {
if (entry.isIntersecting) {
entry.target.classList.add('active');
}
});
}, {
threshold: 0.15,
rootMargin: '0px 0px -50px 0px'
});

revealElements.forEach(el => revealObserver.observe(el));
} else {
// Fallback if no IntersectionObserver support
revealElements.forEach(el => el.classList.add('active'));
}

// ==========================================
// 2. HEADER SCROLL INTERACTION
// ==========================================
const header = document.getElementById('header');

const handleScroll = () => {
if (window.scrollY > 50) {
header.classList.add('scrolled');
} else {
header.classList.remove('scrolled');
}
};

window.addEventListener('scroll', handleScroll);
handleScroll(); // Run once in case page starts scrolled

// ==========================================
// 3. MOBILE HAMBURGER TOGGLE MENU
// ==========================================
const hamburge
/* MISSING LINE 46 */
/* MISSING LINE 47 */
/* MISSING LINE 48 */
/* MISSING LINE 49 */
/* MISSING LINE 50 */
/* MISSING LINE 51 */
/* MISSING LINE 52 */
/* MISSING LINE 53 */
/* MISSING LINE 54 */
};

hamburgerToggle.addEventListener('click', toggleMenu);

// Close menu when clicking navigation links
navLinks.forEach(link => {
link.addEventListener('click', () => {
hamburgerToggle.setAttribute('aria-expanded', 'false');
hamburgerToggle.classList.remove('active');
navMenu.classList.remove('open');
});
});
}

// ==========================================
// 4. EXPANDING CARDS CONTROLLER (Courses)
// ==========================================
const expandingCards = document.querySelectorAll('.expanding-card');

if (expandingCards.length > 0) {
expandingCards.forEach(card => {
const activate = () => {
expandingCards.forEach(c => c.classList.remove('active'));
card.classList.add('active');
};

card.addEventListener('mouseenter', activate);
card.addEventListener('click', activate);
card.addEventListener('focus', activate);
});
}

// ==========================================
// 5. MODAL WINDOW CONTROLLERS
// ==========================================
const applyModal = document.getElementById('apply-modal');
const successModal = document.getElementById('success-modal');
const closeApplyBtn = document.getElementById('close-apply-modal');
const closeSuccessBtn = document.getElementById('close-success-modal');
const btnSuccessOk = document.getElementById('btn-success-ok');

const openApplyButtons = document.querySelectorAll('.open-apply-modal');

const openModal = (modal) => {
if (!modal) return;
modal.classList.add('open');
document.body.style.overflow = 'hidden'; // Lock background scrolling
};

const closeModal = (modal) => {
if (!modal) return;
modal.classList.remove('open');
document.body.style.overflow = ''; // Unlock scrolling
};

openApplyButtons.forEach(btn => {
btn.addEventListener('click', (e) => {
e.stopPropagation(); // Avoid triggering any card events

// Auto-populate course dropdown inside the modal if clicked from a course card
const defaultCourse = btn.getAttribute('data-default-course');
const courseSelect = document.getElementById('apply-course');
if (defaultCourse && courseSelect) {
courseSelect.value = defaultCourse;
}
openModal(applyModal);
});
});

if (closeApplyBtn) {
closeApplyBtn.addEventListener('click', () => closeModal(applyModal));
}

if (closeSuccessBtn) {
closeSuccessBtn.addEventListener('click', () => closeModal(successModal));
}

if (btnSuccessOk) {
btnSuccessOk.addEventListener('click', () => closeModal(successModal));
}

// Close modals when clicking on background overlay
window.addEventListener('click', (e) => {
if (e.target === applyModal) closeModal(applyModal);
if (e.target === successModal) closeModal(successModal);
});

// Close mo
/* MISSING LINE 143 */
/* MISSING LINE 144 */
/* MISSING LINE 145 */
/* MISSING LINE 146 */
/* MISSING LINE 147 */
/* MISSING LINE 148 */
/* MISSING LINE 149 */
/* MISSING LINE 150 */
/* MISSING LINE 151 */
// ==========================================
const demoForm = document.getElementById('demo-form');
const applyForm = document.getElementById('apply-form');

const validateInput = (input) => {
let isValid = true;
const value = input.value.trim();

// Reset error styling
input.style.borderColor = '';

if (input.required && !value) {
isValid = false;
} else if (input.type === 'email' && value) {
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
if (!emailRegex.test(value)) isValid = false;
} else if (input.type === 'tel' && value) {
const phoneRegex = /^\d{10}$/; // Expect 10 digits
// Strip any spaces, dashes or parens to validate 10-digit number
const cleanPhone = value.replace(/[-()\s]/g, '');
if (!phoneRegex.test(cleanPhone)) isValid = false;
}

if (!isValid) {
input.style.borderColor = 'var(--color-error)';
}

return isValid;
};

const handleFormSubmit = (form, successMsg) => {
if (!form) return;

const inputs = form.querySelectorAll('input, select, textarea');
let isFormValid = true;

inputs.forEach(input => {
if (!validateInput(input)) {
isFormValid = false;
}
});

if (isFormValid) {
// Simulate submission loading
const submitBtn = form.querySelector('button[type="submit"]');
const originalText = submitBtn.textContent;
submitBtn.disabled = true;
submitBtn.innerHTML = '<span class="spinner"></span> Submitting...';

setTimeout(() => {
// Success
submitBtn.disabled = false;
submitBtn.textContent = originalText;

// Reset Form
form.reset();

// Close Apply Modal if open
if (applyModal.classList.contains('open')) {
closeModal(applyModal);
}

// Show Success Modal
const successMessageEl = document.getElementById('success-message');
if (successMessageEl && successMsg) {
successMessageEl.textContent = successMsg;
}
openModal(successModal);
}, 1200);
}
};

if (demoForm) {
demoForm.addEventListener('submit', (e) => {
e.preventDefault();
handleFormSubmit(
demoForm,
'Your assessment booking has been registered successfully! One of our coaches will reach out to analyze your level.'
);
});
}

if (applyForm) {
applyForm.addEventListener('submit', (e) => {
e.preventDefault();
handleFormSubmit(
applyForm,
'Your registration has been submitted successfully! One of our coaches will reach out to analyze your level.'
);
});
}

// ==========================================
// 7. LEARNING JOURNEY VERTICAL CAROUSEL CONTROLLER
// ==========================================

expandingCards.forEach(c => c.classList.remove('active'));
card.classList.add('active');
};
card.addEventListener('mouseenter', activate);
card.addEventListener('click', activate);
card.addEventListener('focus', activate);

let currentIndex = 0;
let visibleCount = 1;

// Word reveal intersection observer for title/desc
if ('IntersectionObserver' in window) {
const observer = new IntersectionObserver((entries, obs) => {
entries.forEach(entry => {
if (entry.isIntersecting) {
carouselSection.classList.add('active');

// Trigger Word Appear Animations
const wordElements = carouselSection.querySelectorAll('.word-animate');
wordElements.forEach(word => {
const delay = parseInt(word.getAttribute('data-delay'), 10) || 0;
setTimeout(() => {
if (word) {
word.style.animation = 'word-appear 0.8s ease-out forwards';
}
}, delay);
});

obs.unobserve(entry.target);
}
});
}, { threshold: 0.1 });
observer.observe(carouselSection);
} else {
carouselSection.classList.add('active');
carouselSection.querySelectorAll('.word-animate').forEach(word => {
word.style.animation = 'word-appear 0.8s ease-out forwards';
});
}

const updateVisibleCount = () => {
const width = window.innerWidth;
// In the vertical carousel:
// Desktop/Tablet: 2 slides visible
// Mobile: 1 slide visible
if (width >= 768) {
visibleCount = 2;
} else {
visibleCount = 1;
}
};

const getMaxIndex = () => {
return Math.max(0, slides.length - visibleCount);
};

const updateCarousel = () => {
// Bound check
const maxIndex = getMaxIndex();
if (currentIndex > maxIndex) {
currentIndex = maxIndex;
}
if (currentIndex < 0) {
currentIndex = 0;
}

// Translate track vertically (translateY)
const percentage = -(currentIndex * (100 / visibleCount));
if (track) {
track.style.transform = `translateY(${percentage}%)`;
}

// Enable/disable buttons
if (prevBtn) {
prevBtn.disabled = currentIndex === 0;
}
if (nextBtn) {
nextBtn.disabled = currentIndex === maxIndex;
}

// Update indicator dots
if (indicatorsContainer) {
const dots = indicatorsContainer.querySelectorAll('.carousel-dot');
dots.forEach((dot, idx) => {
if (idx === currentIndex) {
dot.classList.add('active');
} else {
dot.classList.remove('active');
}
});
}
};

const createIndicators = () => {
if (!indicatorsContainer) return;

indicatorsContainer.innerHTML = '';
const totalDots = getMaxIndex() + 1;

for (let i = 0; i < totalDots; i++) {
const dot = document.createElement('button');
dot.type = 'button';
dot.className = 'carousel-dot';
if (i === currentIndex) {
dot.classList.add('active');
}
dot.setAttribute('aria-label', `Go to slide ${i + 1}`);
dot.addEventListener('click', () => {
currentIndex = i;
updateCarousel();
});
indicatorsContainer.appendChild(dot);
}
};

// Initialize
const initCarousel = () => {
updateVisibleCount();
createIndicators();
updateCarousel();
};

initCarousel();

window.addEventListener('resize', () => {
const oldVisibleCount = visibleCount;
updateVisibleCount();
if (oldVisibleCount !== visibleCount) {
createIndicators();
updateCarousel();
}
});

if (prevBtn) {
prevBtn.addEventListener('click', () => {
if (currentIndex > 0) {
currentIndex--;
updateCarousel();
}
});
}

if (nextBtn) {
nextBtn.addEventListener('click', () => {
if (currentIndex < getMaxIndex()) {
currentIndex++;
updateCarousel();
}
});
}
}

// ==========================================
// 8. INTERACTIVE METHODOLOGY TABS CONTROLLER
// ==========================================
const tabTriggers = document.querySelectorAll('.tab-trigger');
const tabPanels = document.querySelectorAll('.tab-panel');

if (tabTriggers.length > 0 && tabPanels.length > 0) {
tabTriggers.forEach(trigger => {
trigger.addEventListener('click', () => {
const targetId = trigger.getAttribute('aria-controls');

// Update tab triggers active states & ARIA
tabTriggers.forEach(t => {
t.classList.remove('active');
t.setAttribute('aria-selected', 'false');
});
trigger.classList.add('active');
trigger.setAttribute('aria-selected', 'true');

// Update panels active states
tabPanels.forEach(p => {
p.classList.remove('active');
});
const targetPanel = document.getElementById(targetId);
if (targetPanel) {
targetPanel.classList.add('active');
}

// Smoothly scroll the selected tab button into view on mobile devices
trigger.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
});
});
}

// ==========================================
// 8b. INTERACTIVE GRAMMAR SUB-TABS CONTROLLER
// ==========================================
const subtabTriggers = document.querySelectorAll('.subtab-trigger');
const subpanels = document.querySelectorAll('.subpanel');

if (subtabTriggers.length > 0 && subpanels.length > 0) {
subtabTriggers.forEach(trigger => {
trigger.addEventListener('click', () => {
const targetId = trigger.getAttribute('aria-controls');

// Update sub-tab triggers active states & ARIA
subtabTriggers.forEach(t => {
t.classList.remove('active');
t.setAttribute('aria-selected', 'false');
});
trigger.classList.add('active');
trigger.setAttribute('aria-selected', 'true');

// Update subpanels active states
subpanels.forEach(p => {
p.classList.remove('active');
});
const targetPanel = document.getElementById(targetId);
if (targetPanel) {
targetPanel.classList.add('active');
}
// Append a space after each word except the last one
if (wordIdx < words.length - 1) {
const spaceSpan = document.createElement('span');
spaceSpan.className = 'split-char-space';
spaceSpan.innerHTML = '&nbsp;';
fragment.appendChild(spaceSpan);
}
});

el.appendChild(fragment);
});

// Animate with GSAP if loaded
if (window.gsap && window.ScrollTrigger) {
gsap.registerPlugin(ScrollTrigger);

splitTextElements.forEach(el => {
const chars = el.querySelectorAll('.split-char-item');

const isHero = el.classList.contains('hero-title');
const delayVal = isHero ? 0.2 : 0.05;
const staggerVal = isHero ? 0.03 : 0.015;
const durationVal = isHero ? 0.8 : 0.6;

gsap.fromTo(chars,
{
opacity: 0,
y: 35
},
{
opacity: 1,
y: 0,
duration: durationVal,
ease: "power3.out",
stagger: staggerVal,
delay: delayVal,
scrollTrigger: {
trigger: el,
start: "top 85%",
once: true,
fastScrollEnd: true
}
}
);
});
} else {
document.querySelectorAll('.split-char-item').forEach(char => {
char.style.opacity = '1';
});
}

});


if (window.anime) {
const whyIconPaths = document.querySelectorAll('.why-icon svg path, .why-icon svg circle, .why-icon svg polygon');

whyIconPaths.forEach(path => {
const length = path.getTotalLength ? path.getTotalLength() : 150;
path.style.strokeDasharray = length;
path.style.strokeDashoffset = length;
});

anime({
targets: '.why-icon svg path, .why-icon svg circle, .why-icon svg polygon',
strokeDashoffset: [
function(el) { return el.getTotalLength ? el.getTotalLength() : 150; },
0
],
easing: 'easeInOutQuad',
duration: 1200,
loop: true,
direction: 'alternate',
delay: function(el, i) { return i * 200; }
});
}
});


/* MISSING LINE 540 */
/* MISSING LINE 541 */
/* MISSING LINE 542 */
/* MISSING LINE 543 */
/* MISSING LINE 544 */
/* MISSING LINE 545 */
/* MISSING LINE 546 */
/* MISSING LINE 547 */
/* MISSING LINE 548 */
/* MISSING LINE 549 */
/* MISSING LINE 550 */
/* MISSING LINE 551 */
/* MISSING LINE 552 */
/* MISSING LINE 553 */
/* MISSING LINE 554 */
/* MISSING LINE 555 */
/* MISSING LINE 556 */
/* MISSING LINE 557 */
/* MISSING LINE 558 */
/* MISSING LINE 559 */
/* MISSING LINE 560 */
/* MISSING LINE 561 */
/* MISSING LINE 562 */
/* MISSING LINE 563 */
/* MISSING LINE 564 */
/* MISSING LINE 565 */
/* MISSING LINE 566 */
/* MISSING LINE 567 */
/* MISSING LINE 568 */
/* MISSING LINE 569 */
/* MISSING LINE 570 */
/* MISSING LINE 571 */
/* MISSING LINE 572 */
/* MISSING LINE 573 */
/* MISSING LINE 574 */
/* MISSING LINE 575 */
/* MISSING LINE 576 */
/* MISSING LINE 577 */
/* MISSING LINE 578 */
/* MISSING LINE 579 */
});
}

// Pointer/Drag events for the front card
let startY = 0;
// 13. PREMIUM GSAP SPLIT-TEXT REVEAL
// ==========================================
const splitTextElements = document.querySelectorAll('.split-text-animate');

splitTextElements.forEach(el => {
const text = el.textContent.trim();
el.textContent = '';

const fragment = document.createDocumentFragment();
for (let char of text) {
const span = document.createElement('span');
/* MISSING LINE 596 */
/* MISSING LINE 597 */
/* MISSING LINE 598 */
/* MISSING LINE 599 */
activeFrontCard.style.cursor = 'grabbing';
};

const onPointerMove = (e) => {
if (!isDragging || !activeFrontCard) return;

const currentY = e.clientY !== undefined ? e.clientY : e.touches[0].clientY;
dragY = currentY - startY;

// Limit elastic drag
const dragElastic = dragY * 0.7;

// Calculate rotation and opacity (transformations)
// range [-200, 0, 200] -> [15, 0, -15] rotation
const rot = Math.max(-15, Math.min(15, -(dragElastic / 200) * 15));
const op = Math.max(0, 1 - Math.abs(dragElastic) / 250);

activeFrontCard.style.transform = `translateY(${dragElastic}px) rotateX(${rot}deg) scale(1.02)`;
activeFrontCard.style.opacity = op;
};

const onPointerUp = () => {
if (!isDragging || !activeFrontCard) return;
isDragging = false;

activeFrontCard.style.transition = '';
activeFrontCard.style.cursor = '';

if (Math.abs(dragY) > swipeThreshold) {
if (dragY < 0) {
// Swipe up
moveToEnd();
} else {
// Swipe down
moveToStart();
}
} else {
// Reset card
updateStack();
}
activeFrontCard = null;
};

// Attach listeners to container viewport to handle drag cleanly outside the bounds
const viewport = benefitsSection.querySelector('.card-stack-viewport');

viewport.addEventListener('mousedown', onPointerDown);
window.addEventListener('mousemove', onPointerMove);
window.addEventListener('mouseup', onPointerUp);

// Touch events for mobile
viewport.addEventListener('touchstart', onPointerDown, { passive: true });
window.addEventListener('touchmove', onPointerMove, { passive: false });
window.addEventListener('touchend', onPointerUp);

// Initialize stack
updateStack();
}

// ==========================================
// 13. PREMIUM GSAP SPLIT-TEXT REVEAL
// ==========================================
const splitTextElements = document.querySelectorAll('.split-text-animate');

splitTextElements.forEach(el => {
const text = el.textContent.trim();
el.textContent = '';

const fragment = document.createDocumentFragment();
for (let char of text) {
const span = document.createElement('span');
