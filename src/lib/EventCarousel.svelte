<script lang="ts">
	import { onMount } from 'svelte';

	import emblaCarouselSvelte from 'embla-carousel-svelte';
	import Autoplay from 'embla-carousel-autoplay';

	let options = { loop: true };
	let plugins = [Autoplay({delay: 4000})];

	onMount(() => {});
</script>

<div class="embla">
	<div class="embla__viewport" use:emblaCarouselSvelte={{ options, plugins }}>
		<div class="embla__container">
			<div class="embla__slide">
				<img
					class="embla__slide__img"
					src="/assets/events/board-games-night-2023/3.JPG"
					alt="Your alt text"
				/>
			</div>
			<div class="embla__slide">
				<img
					class="embla__slide__img"
					src="/assets/events/board-games-night-2023/4.JPG"
					alt="Your alt text"
				/>
			</div>
			<div class="embla__slide">
				<img
					class="embla__slide__img"
					src="/assets/events/board-games-night-2023/6.JPG"
					alt="Your alt text"
				/>
			</div>
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
</style>
