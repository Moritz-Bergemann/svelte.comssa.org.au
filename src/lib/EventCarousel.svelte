<script lang="ts">
	import { onMount } from 'svelte';
	import type { EmblaCarouselType } from 'embla-carousel';
	import emblaCarouselSvelte from 'embla-carousel-svelte';
	import Autoplay from 'embla-carousel-autoplay';

	export let imageLinks: string[];

	// Scale tweening. Source: https://www.embla-carousel.com/examples/predefined/#scale
	const TWEEN_FACTOR_SCALE = 0.5;

	const calculateTweenValuesScale = (emblaApi: EmblaCarouselType): number[] => {
		const engine = emblaApi.internalEngine();
		const scrollProgress = emblaApi.scrollProgress();

		return emblaApi.scrollSnapList().map((scrollSnap, index) => {
			if (!emblaApi.slidesInView().includes(index)) return 0;
			let diffToTarget = scrollSnap - scrollProgress;

			if (engine.options.loop) {
				engine.slideLooper.loopPoints.forEach((loopItem) => {
					const target = loopItem.target();
					if (index === loopItem.index && target !== 0) {
						const sign = Math.sign(target);
						if (sign === -1) diffToTarget = scrollSnap - (1 + scrollProgress);
						if (sign === 1) diffToTarget = scrollSnap + (1 - scrollProgress);
					}
				});
			}
			const tweenValue = 1 - Math.abs(diffToTarget * TWEEN_FACTOR_SCALE);
			return numberWithinRange(tweenValue, 0, 1);
		});
	};

	export const setupTweenScale = (
		emblaApi: EmblaCarouselType
	): {
		applyTweenScale: () => void;
		removeTweenScale: () => void;
	} => {
		const tweenNodes = <HTMLElement[]>(
			emblaApi.slideNodes().map((slideNode) => slideNode.querySelector('.embla__scale'))
		);

		const applyTweenScale = (): void => {
			const tweenValues = calculateTweenValuesScale(emblaApi);
			tweenValues.forEach((tweenValue, index) => {
				tweenNodes[index].style.transform = `scale(${tweenValue})`;
			});
		};

		const removeTweenScale = (): void => {
			tweenNodes.forEach((slide) => slide.removeAttribute('style'));
		};

		return {
			applyTweenScale,
			removeTweenScale
		};
	};

	// Opacity tweening. Retrieved from https://www.embla-carousel.com/examples/predefined/#opacity
	const TWEEN_FACTOR_OPACITY = 2;

	const numberWithinRange = (number: number, min: number, max: number): number =>
		Math.min(Math.max(number, min), max);

	const calculateTweenValuesOpacity = (emblaApi: EmblaCarouselType): number[] => {
		const engine = emblaApi.internalEngine();
		const scrollProgress = emblaApi.scrollProgress();

		return emblaApi.scrollSnapList().map((scrollSnap, index) => {
			if (!emblaApi.slidesInView().includes(index)) return 0;
			let diffToTarget = scrollSnap - scrollProgress;

			if (engine.options.loop) {
				engine.slideLooper.loopPoints.forEach((loopItem) => {
					const target = loopItem.target();
					if (index === loopItem.index && target !== 0) {
						const sign = Math.sign(target);
						if (sign === -1) diffToTarget = scrollSnap - (1 + scrollProgress);
						if (sign === 1) diffToTarget = scrollSnap + (1 - scrollProgress);
					}
				});
			}
			const tweenValue = 1 - Math.abs(diffToTarget * TWEEN_FACTOR_OPACITY);
			return numberWithinRange(tweenValue, 0, 1);
		});
	};

	export const setupTweenOpacity = (
		emblaApi: EmblaCarouselType
	): {
		applyTweenOpacity: () => void;
		removeTweenOpacity: () => void;
	} => {
		const tweenNodes = emblaApi.slideNodes();

		const applyTweenOpacity = (): void => {
			const tweenValues = calculateTweenValuesOpacity(emblaApi);
			tweenValues.forEach((tweenValue, index) => {
				tweenNodes[index].style.opacity = tweenValue.toString();
			});
		};

		const removeTweenOpacity = (): void => {
			tweenNodes.forEach((slide) => slide.removeAttribute('style'));
		};

		return {
			applyTweenOpacity,
			removeTweenOpacity
		};
	};

	let options = { loop: true, inViewThreshold: -0.5 };
	let plugins = [Autoplay({ delay: 4000, stopOnInteraction: false })];

	const onInit = (event: CustomEvent<EmblaCarouselType>) => {
		let emblaApi = event.detail;

		let { applyTweenOpacity, removeTweenOpacity } = setupTweenOpacity(emblaApi);
		let { applyTweenScale, removeTweenScale } = setupTweenScale(emblaApi);

		emblaApi
			// Opacity
			.on('init', applyTweenOpacity)
			.on('scroll', applyTweenOpacity)
			.on('reInit', applyTweenOpacity)
			.on('destroy', removeTweenOpacity)

			// Scaling
			.on('init', applyTweenScale)
			.on('scroll', applyTweenScale)
			.on('reInit', applyTweenScale)
			.on('destroy', removeTweenScale);

		applyTweenOpacity();
		applyTweenScale();
	};

	onMount(() => {});
</script>

<div class="embla">
	<div class="embla__viewport" use:emblaCarouselSvelte={{ options, plugins }} on:emblaInit={onInit}>
		<div class="embla__container">
			{#each imageLinks as imageLink}
				<div class="embla__slide">
					<div class="embla__scale">
						<img class="embla__slide__img" src={imageLink} alt="Your alt text" />
					</div>
				</div>
			{/each}
		</div>
	</div>
</div>

<style>
	.embla {
		--slide-spacing: 10rem;
		--slide-size: 75%;
		--slide-height: 24rem;
		padding: 1.6rem;
	}
	.embla__viewport {
		overflow: visible;
	}
	.embla__container {
		backface-visibility: hidden;
		display: flex;
		touch-action: pan-y;
		margin-left: calc(var(--slide-spacing) * -1);
	}
	.embla__slide {
		flex: 0 0 var(--slide-size);
		min-width: 0;
		padding-left: var(--slide-spacing);
		position: relative;
	}
	.embla__slide__img {
		display: block;
		height: var(--slide-height);
		width: 100%;
		object-fit: cover;
	}
	.embla__scale {
		height: 100%;
		position: relative;
		backface-visibility: hidden;
	}
</style>
