<script lang="ts">
	import Fa from 'svelte-fa/src/fa.svelte';
	import {
		faDiscord,
		faFacebookSquare,
		faGithub,
		faLinkedin,
		faInstagram
	} from '@fortawesome/free-brands-svg-icons';

    export let color: string;
    export let logoSize: string = "2rem";
</script>

<div class="logo-container">
	<a href="https://discord.gg/SuwfFfjYJB"><Fa icon={faDiscord} color={color} size={logoSize} /></a
	>
	<a href="https://www.facebook.com/ComSSACurtin/"
		><Fa icon={faFacebookSquare} color={color} size={logoSize} /></a
	>
	<a href="https://linkedin.com/company/computer-science-students-association"
		><Fa icon={faLinkedin} color={color} size={logoSize} /></a
	>
	<a href="https://www.instagram.com/comssacurtin/"
		><Fa icon={faInstagram} color={color} size={logoSize} /></a
	>
	<a href="https://github.com/ComSSA/"><Fa icon={faGithub} color={color} size={logoSize} /></a>
</div>

<style>
    .logo-container {
		display: flex;
		flex-direction: row;
		flex-wrap: wrap;
		justify-content: space-evenly;
		margin: auto;
		max-width: 18rem;
    }

	.logo-container Fa {
	}
</style>