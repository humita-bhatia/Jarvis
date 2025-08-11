/*
const { styleText } = require("util");

$(document).ready(function () {

    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",
        },
        out: {
            effect: "bounceOut"
        },
    });
    //Siri Wave Configuration
    var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 640,
    height: 200,
    style: "ios9",
    autostart:true,
    speed: 0.2,
    amplitude: 1,
  });
});
*/


$(window).on('load', function () {
    // Textillate animations
    $('.text').textillate({
        loop: true,
        sync: true,
        in: { effect: "bounceIn" },
        out: { effect: "bounceOut" }
    });

    // SiriWave setup
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        autostart: true,
        speed: 0.22,
        amplitude: 2,
    });
    //Siri Message Animation
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true,
        },
        out: {
            effect: "fadeOutUp",
            sync: true,
        },
    });

});


    $("#MicButton").click(function () {
        try {
            eel.play_startup_sound();
        } catch (error) {
            console.error("Eel call failed:", error);
        }

        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);

        eel.takecommand()().then(function (result) {
            console.log("Python returned:", result);
            $("#SiriWave").attr("hidden", true);
            $("#Oval").attr("hidden", false);
        }).catch(function (err) {
            console.error("Eel takecommand error:", err);
        });
    });




    //Mic button click event

    //     $("#MicButton").click(function () {

    //         //Cal the python function --- not working yet  
    //         try {
    //             eel.play_startup_sound();  // This will fail silently if HTML opened directly
    //         } catch (error) {
    //             console.error("Eel call failed:", error);
    //         }

    //         //Toggle visibility 
    //         $("#Oval").attr("hidden", true);
    //         $("#SiriWave").attr("hidden", false);

    //         eel.takecommand();
    //     });

    // });
    // function onMicClick() {
    //     eel.start_listening()(function(response) {
    //         console.log("You said:", response);
    //     });
    // }