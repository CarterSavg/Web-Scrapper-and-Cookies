// Carter Savage 1103661
$(document).ready(function() {
    console.log("Carter Savage\nStudent Number: 1103661");
    $("#selectMenu").html('<label>Select your source</label><form action="#" method="post" name = "inputForm"><input type="button" id = "getApexKeys" value = "Get ApexKeys Products"><input type="button" id = "getMinoKeys" value = "Get Mino Keys Products"></button><input type="button" id = "getMechMarket" value  = "Get r/MechMarket"></button></form>');
    if ($("#bodyInfo").html ===""){
        $("#bodyInfo").html("Truely only the coolest of coders are able create a hub of the finest keebs such as this. Click one of the buttons below to display that subreddit's news. Click CCKN&trade; in the top left corner to go back to the home page.")
    }
        
    // Button functionality
    $("#getApexKeys").click(function(){
        $.ajax({url: "/ApexKeys", success: function(result){
            $("#bodyInfo").html(result);
            $("#links").html("");
        }});
    });
    $("#getMinoKeys").click(function(){
        $.ajax({url: "/MinoKeys", success: function(result){
            $("#bodyInfo").html(result);
            $("#links").html("");
        }});
    });
    $("#getMechMarket").click(function(){
        $.ajax({url: "/MechMarket", success: function(result){
            $("#bodyInfo").html(result);
            $("#links").html("");
        }});
    });
});
