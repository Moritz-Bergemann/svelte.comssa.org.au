<style>
    :root {
        --comssa-blue: #4459a5;
        --comssa-secondary-blue: #7ea3cc;
        --comssa-orange: #f5831f;
        --comssa-black: #404040;
    }
    .comssa-logo {
        letter-spacing: 0.15rem;
        line-height: 1;
        font-family: 'Wavehaus Bold';
        font-size: 90px;
        margin-top: 0;
        margin-bottom: 0;
        position: absolute;
        top: 100px;
        left: 200px;
    }

    .join-button { 
        font-family: 'Wavehaus Bold';
        letter-spacing: 0.15rem;

        background-color: blue; /* Green */
        border: none;
        color: white;
        padding: 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;

        border-radius: 15px;

        position: absolute;
        top: 500px;
        left: 200px;
    }


    .commsa-blue-text {
        color: var(--comssa-blue)
    }

    .comssa-black-text {
        color: var(--comssa-black)
    }

    #navbar {
        width: 100%;
        height: 80px;
        background-color: var(--comssa-blue);
        text-align: center;
    }

    .navbar-items {
        padding-left: 10%;
        padding-right: 10%;
        height: 100%;
        display: flex;
        flex-direction: row;
        align-items: center;
    }

    .navbar-items div {
        max-width: 150px;
        flex: auto;
        margin-left: auto;
        margin-right: auto;
        text-align: center;
    }

    #landing-screen {
        height: 100vh;
        /* TODO replace this gross gradient with a pretty background*/
        background-image: linear-gradient(to bottom, white, var(--comssa-secondary-blue));
        position: relative;
    }

    .content {
        max-width: 60em ; 
        margin: auto;
    }

    h1 {
        font-family: "Wavehaus SemiBold";
        letter-spacing: 0.15rem;
    }
</style>

<script lang="ts">
    import {onMount, onDestroy} from 'svelte'
    import "../styles/app.css";

    onMount(() => {
        const SHOW_SCROLL_NAVBAR_HEIGHT = 20;

        let showNavbar: boolean = true;

        // window.onscroll = () => {
        //     if (window.scrollY > SHOW_SCROLL_NAVBAR_HEIGHT) {
        //         console.log("there!");
        //         showNavbar = true;
        //     } else {
        //         console.log("not there!");
        //         showNavbar = false;
        //     }
        // }
    })
</script>


<main>
    <div id="landing-screen">
        <div>
            <p class="comssa-logo">
                <span class="commsa-blue-text">Com</span><span class="comssa-black-text">puter</span> <br>
                <span class="commsa-blue-text">S</span><span class="comssa-black-text">cience</span> <br>
                <span class="commsa-blue-text">S</span><span class="comssa-black-text">tudents</span> <br>
                <span class="commsa-blue-text">A</span><span class="comssa-black-text">ssociation</span>
            </p>
        </div>

        <a class="join-button" href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">Join Now!</a>
    </div>

    <div class="content">
        <div>
            <h1>Who are we?</h1>

            <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi non tristique lacus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Quisque in blandit purus. Nulla odio ante, volutpat id aliquam quis, pharetra eget urna. Proin sollicitudin ipsum sapien, aliquam porttitor dui maximus eget. Vivamus bibendum tristique libero sit amet porttitor. Pellentesque eu facilisis nibh. Maecenas ac sapien a justo rhoncus pretium vitae vel est. Suspendisse ornare sodales est, quis mattis orci dignissim vitae. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.

                Mauris sit amet arcu eu enim hendrerit bibendum id nec magna. Donec in augue vel erat dapibus suscipit. Ut eu bibendum lacus. Pellentesque ultrices ipsum id nunc venenatis, ac condimentum erat tincidunt. Nam sagittis blandit ipsum vel molestie. Morbi ultricies non nunc et molestie. Morbi volutpat pulvinar odio ut tincidunt. Fusce pharetra vehicula rhoncus. Nullam nibh dolor, efficitur sit amet leo eu, volutpat faucibus velit. Vivamus tincidunt, enim in ultrices porta, enim mi lacinia mi, eget feugiat mi felis maximus odio. Donec rhoncus at libero at suscipit.
                
                Etiam molestie ante vel lacinia porttitor. Nullam posuere risus tellus, eget ornare quam congue eu. Fusce sodales viverra ex, quis ultricies arcu blandit et. Duis vitae sagittis sem. In quis velit ut leo convallis dapibus nec at eros. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam erat volutpat.
                
                Aenean viverra leo ut justo gravida, eu aliquam neque convallis. Pellentesque nibh mauris, ornare eu malesuada nec, fermentum vel mi. In turpis mauris, porttitor et tellus sit amet, venenatis porttitor ex. Nulla dictum condimentum sem. Sed vel libero eu tortor sollicitudin euismod vel vel turpis. Ut varius velit nec semper lobortis. Cras odio risus, elementum cursus ipsum egestas, iaculis tristique neque. Aliquam venenatis egestas sagittis. Nulla lacinia tellus at libero faucibus, a posuere arcu sagittis. Nunc in dignissim quam. Pellentesque eu augue metus. Vestibulum id dignissim metus. Nam sed interdum magna. 
            </p>
            
        </div>
    </div>
    <!-- <div id="navbar">
        <div class="navbar-items">
            <div>bean1</div>
            <div>bean2</div>
            <div>bean3</div>
        </div>
    </div> -->


    <div style="max-width: 60em ; margin: auto;">

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi non tristique lacus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Quisque in blandit purus. Nulla odio ante, volutpat id aliquam quis, pharetra eget urna. Proin sollicitudin ipsum sapien, aliquam porttitor dui maximus eget. Vivamus bibendum tristique libero sit amet porttitor. Pellentesque eu facilisis nibh. Maecenas ac sapien a justo rhoncus pretium vitae vel est. Suspendisse ornare sodales est, quis mattis orci dignissim vitae. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.

        Mauris sit amet arcu eu enim hendrerit bibendum id nec magna. Donec in augue vel erat dapibus suscipit. Ut eu bibendum lacus. Pellentesque ultrices ipsum id nunc venenatis, ac condimentum erat tincidunt. Nam sagittis blandit ipsum vel molestie. Morbi ultricies non nunc et molestie. Morbi volutpat pulvinar odio ut tincidunt. Fusce pharetra vehicula rhoncus. Nullam nibh dolor, efficitur sit amet leo eu, volutpat faucibus velit. Vivamus tincidunt, enim in ultrices porta, enim mi lacinia mi, eget feugiat mi felis maximus odio. Donec rhoncus at libero at suscipit.
        
        Etiam molestie ante vel lacinia porttitor. Nullam posuere risus tellus, eget ornare quam congue eu. Fusce sodales viverra ex, quis ultricies arcu blandit et. Duis vitae sagittis sem. In quis velit ut leo convallis dapibus nec at eros. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam erat volutpat.
        
        Aenean viverra leo ut justo gravida, eu aliquam neque convallis. Pellentesque nibh mauris, ornare eu malesuada nec, fermentum vel mi. In turpis mauris, porttitor et tellus sit amet, venenatis porttitor ex. Nulla dictum condimentum sem. Sed vel libero eu tortor sollicitudin euismod vel vel turpis. Ut varius velit nec semper lobortis. Cras odio risus, elementum cursus ipsum egestas, iaculis tristique neque. Aliquam venenatis egestas sagittis. Nulla lacinia tellus at libero faucibus, a posuere arcu sagittis. Nunc in dignissim quam. Pellentesque eu augue metus. Vestibulum id dignissim metus. Nam sed interdum magna. 
    </div>
</main>