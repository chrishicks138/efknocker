# EFknockr
> internet relay chat beacon

## Warning
This repository was made for testing against your own server(s). I am not responsible for how the public uses these.
For any questions, comments, & concerns, please join #5000 on irc.supernets.org

## Information
This is basically an IRC drive-by. It takes a list of IRC servers, connects to all of them & join every channel to send a custom message. You can also have it mass highlight & mass private message the channels for more attention to your message. It will do various things to make sure it does not get banned, throttled, or detected. Alter the throttle settings with caution as they are the sane defaults for max results.

The humor behind this script is that anyone can mass portscan 0.0.0.0/0 *(the entire IPv4 range)* for port 6667 & essentially send a message to every IRC server on the internet. But I have heard a rumor that doing so will only affect channels that are boring, lame, & shitty :) :) :)

## Settings
| Setting     | Default Value  | Description                                      |
| ----------- | -------------- | ------------------------------------------------ |
| mass_hilite | True           | Hilite all the users in a channel before parting |
| part_msg    | 'Smell ya l8r' | Send a custom part message when leaving channels |
| proxy       | None           | Proxy should be a Socks5 in IP:PORT format       |
| register    | True           | Register with NickServ before joining channels   |
| vhost       | None           | Use a virtual host on all connections            |

## Throttle
| Setting     | Default Value  | Description                                                  |
| ----------- | -------------- | ------------------------------------------------------------ |
| channels    | 3              | Maximum number of channels to be flooding at once            |
| delay       | 30             | Delay before registering nick *(if enabled)* and sending /LIST |
| join        | 3              | Delay between each channel join                              |
| message     | 0.5            | Delay between each message sent to a channel                 |
| private     | 0.5            | Delay between each private message sent                      |
| threads     | 100            | Maximum number of threads running                            |
| timeout     | 5              | Timeout for all sockets                                      |
| users       | 10             | Minimum number of users required in a channel                |

**Note:** The default throttles are set to make harder to detect & mitigate this script.

## Todo
* Use asyncio library
* CTCP VERSION replies
* Convert text with unicode, combining diacritics & zero-width characters.
* Analytics modes (Collect information such as server name, host, version, map, channels, nicks, and hosts for a massive IRC database)
* Check UnrealIRCd default flood throttles.
* Use of identd
* Weechat DCC buffer-overlfow exploit *(See [here](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-8073))*
* OpenSSL crash exploit *(See [here](https://forums.unrealircd.org/viewtopic.php?f=1&t=9085))*
 
## Mirrors
- [acid.vegas](https://acid.vegas/efknockr) *(main)*
- [GitHub](https://github.com/acidvegas/efknockr)
- [GitLab](https://gitlab.com/acidvegas/efknockr)

# efknocker
