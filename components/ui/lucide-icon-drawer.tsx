import { animate, svg } from 'animejs';
import { useEffect, useRef } from 'react';

export function useLucideDrawerAnimation() {
  const root = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    if (root.current) {
      const svgElements = root.current.querySelectorAll('svg path, svg circle, svg polyline');
      svgElements.forEach((element) => element.classList.add('line'));
      
      // animejs v4 svg drawable path animation
      animate(svg.createDrawable('.line'), {
        draw: ['0 0.05', '0.05 1'],
        ease: 'inOutQuad',
        duration: 1000,
        loop: true,
        alternate: true,
        playbackrate: 1,
      });
    }
  }, []);

  return root;
}
