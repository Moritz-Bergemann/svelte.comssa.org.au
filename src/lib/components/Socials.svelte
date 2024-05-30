<script lang="ts">
	import Fa from 'svelte-fa';
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
	<a href="https://discord.gg/SuwfFfjYJB"><Fa icon={faDiscord} color={color == "original" ? "#5865F2" : color} size={logoSize} /></a
	> 
	<a href="https://www.facebook.com/ComSSACurtin/"
		><Fa icon={faFacebookSquare} color={color == "original" ? "#3B5998" : color} size={logoSize} /></a
	>
	<a href="https://linkedin.com/company/computer-science-students-association"
		><Fa icon={faLinkedin} color={color == "original" ? "#0077B5" : color} size={logoSize} /></a
	>
	<a href="https://www.instagram.com/comssacurtin/"
		><Fa icon={faInstagram} color={color == "original" ? "#C13584" : color} size={logoSize} /></a
	>
	<a href="https://github.com/ComSSA/"><Fa icon={faGithub} color={color == "original" ? "#333" : color} size={logoSize} /></a>
</div>

<style>
    .logo-container {
		display: flex;
		width: 100%;
		flex-direction: row;
		flex-wrap: wrap;
		justify-content: space-evenly;
		margin: auto;
    }
</style>