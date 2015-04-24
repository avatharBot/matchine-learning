// Global variables declaration
var results = {};
var champions = [];
var control = [];
var damage = [];
var economy = [];
var kills = [];
var multi_kills = [];

var champion_list = {};
var match_list = [
    158107613,
    158641787,
    159273124,
    159463481,
    159465089,
    159716798,
    159728037,
    159899741,
    159918696,
    160163547
];


// run on-load
$(function() {
	jQuery.ajaxSetup({
		async: false
	});

	$.ajax({
		dataType: "json",
		url: 'https://global.api.pvp.net/api/lol/static-data/lan/v1.2/champion?locale=en_US&dataById=true&api_key=d61fc939-8323-4f7b-8dc0-0b1b5de2f4b0',
		async: false,
		success: function(data) {
			champion_list = data.data;
		}
	});



    $('#start').click(function(e){
        console.log('start parsing');
        e.preventDefault();
        match_list = $('#matches').val().split(',');

        match_list.forEach(function (mId) {
            matchParser(parseInt(mId));
        });
        // after loop, build results varible
        results = {
            'champions': champions,
            'control': control,
            'damage': damage,
            'economy': economy,
            'kills': kills,
            'multi_kills': multi_kills
        };
        // print on console and screen
        var json = JSON.stringify(results);
        console.log(json);
        $('#stats').val(json);
        $('form').submit();
    });
});


var getChampionName = function(champId) {
	return champion_list[champId].name;
};

var matchParser = function(matchId) {
    var url = 'https://lan.api.pvp.net/api/lol/lan/v2.2/match/'+ matchId +'?includeTimeline=false&api_key=d61fc939-8323-4f7b-8dc0-0b1b5de2f4b0'

	$.ajax({
		dataType: "json",
		url: url,
		async: false,
		success: function(match) {

			match.participants.forEach(function(champ) {
				champions.push(getChampionName(champ.championId));
				// control
				ctrl_data = [
					champ.stats.wardsPlaced,
					champ.stats.wardsKilled
				];
				control.push(ctrl_data);
				// damage
				dmg_data = [
					champ.stats.physicalDamageDealt,
					champ.stats.magicDamageDealt,
					champ.stats.trueDamageDealt,
				];
				damage.push(dmg_data);
				// economy
				econ_data = [
					champ.stats.goldEarned,
					champ.stats.goldSpent,
				];
				economy.push(econ_data)
					// kills
				kda_data = [
					champ.stats.kills,
					champ.stats.deaths,
					champ.stats.assists,
				];
				kills.push(kda_data);
				// multi kills
				combos = champ.stats.doubleKills +
					champ.stats.tripleKills +
					champ.stats.quadraKills + champ.stats
					.pentaKills +
					champ.stats.unrealKills;
				mk_data = [
					combos,
					champ.stats.killingSprees,
					champ.stats.largestKillingSpree
				];
				multi_kills.push(mk_data);
			});
		}
	});
};
