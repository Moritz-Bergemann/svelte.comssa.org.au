<script lang="ts">
	export let name: string;
	export let title: string | null = null;
	export let imageSource: string;
</script>

<div class="profile">
	<img src={imageSource} alt={name} />
	<p class="name">{name}</p>
	{#if title}
		<p class="title">{title}</p>
	{/if}
</div>

<style>
	.profile {
		margin: 1rem;
		max-width: 20rem;
		align-content: center;
	}

	img {
		max-width: 100%;
		max-height: 20rem;
		border-radius: 2rem;
		margin-left: auto;
		margin-right: auto;
		display: block;
	}

	.name {
		text-align: center;
		font-family: WaveHaus Bold;
        font-size: 1.5rem;
        margin-top: 0.5rem;
        margin-bottom: 0;
	}

	.title {
        margin: 0;
		text-align: center;
		font-family: WaveHaus Bold;
        font-size: 1rem;
	}
</style>
