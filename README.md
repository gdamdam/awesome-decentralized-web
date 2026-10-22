# Awesome Decentralized Web [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of peer-to-peer, federated, and local-first protocols, applications, and developer tools. Inspired by the [Decentralized Web Summit](https://web.archive.org/web/2018/https://www.decentralizedweb.net/).

**Scope.** Peer-to-peer protocols, federated applications, and distributed data: projects where decentralization is the core design, not a feature or a marketing claim.

**Out of scope:** cryptocurrencies, blockchains, tokens and other finance projects, AI tools, and commercial products without open-source relevance. Merely using an existing blockchain as a neutral public record can qualify; see the contributing guide.

**Tags.** **Dormant** entries still work but their repository has been inactive for over 2 years. Dead projects live in the Graveyard. Read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting a project.

**Four words that often get mixed up:**

- **Federated** — independent servers interoperating through a shared protocol; you choose which server to trust. *(Mastodon, Matrix, XMPP)*
- **Peer-to-peer** — participants exchange data directly, with no authoritative application server; trackers, bootstrap nodes or relays may assist. *(BitTorrent, Scuttlebutt, Tox)*
- **Distributed** — data or computation spread across many machines; decentralized only when no single party controls it.
- **Local-first** — the authoritative copy of your data lives on your own device and syncs when connectivity allows. *(Automerge, Yjs, Willow)*

## Contents

- [Protocols and Technologies](#protocols-and-technologies)
  - [Federation & Social Protocols](#federation--social-protocols)
  - [P2P Networking & Data Transfer](#p2p-networking--data-transfer)
  - [Application Frameworks](#application-frameworks)
  - [Local-first & CRDTs](#local-first--crdts)
  - [Mesh & Off-grid Networking](#mesh--off-grid-networking)
  - [Identity & Personal Data](#identity--personal-data)
- [Applications](#applications)
  - [Social Networks (Fediverse & beyond)](#social-networks-fediverse--beyond)
  - [Media Streaming & Publishing](#media-streaming--publishing)
  - [P2P Messaging](#p2p-messaging)
  - [Code & Collaboration](#code--collaboration)
  - [File Storage, Sync and Sharing](#file-storage-sync-and-sharing)
  - [Databases](#databases)
  - [Anonymity & Overlay Networks](#anonymity--overlay-networks)
  - [Web, Search and Archiving](#web-search-and-archiving)
  - [Identity & Key Management](#identity--key-management)
- [Decentralization at a Glance](#decentralization-at-a-glance)
- [Choose by Goal](#choose-by-goal)
- [Graveyard](#graveyard)
- [Other Related Lists](#other-related-lists)
- [Contributors](#contributors)

## Protocols and Technologies
*Protocols, stacks and building blocks for a decentralized web.*

### Federation & Social Protocols
- [ActivityPub](https://www.w3.org/TR/activitypub/) - W3C Recommendation (2018) for federated social networking, defining server-to-server and client-to-server APIs; the protocol behind most of the Fediverse.
- [AT Protocol](https://github.com/bluesky-social/atproto) - The Authenticated Transfer Protocol, an open protocol for decentralized social networking with portable identities (DIDs), powering Bluesky; global views of the network rely on resource-intensive Relay and AppView services.
- [ForgeFed](https://github.com/forgefed/forgefed) - ActivityPub extension for federating software forges: a server-to-server API for pull requests, forks, and subscriptions; implemented experimentally by Forgejo.
- [Matrix](https://matrix.org/) - Open specification for federated, persistent communication rooms whose history is replicated across every participating homeserver rather than owned by one; bridges connect it to other chat networks.
- [Nostr](https://nostr.com/) - Minimal protocol in which cryptographically signed notes are published to any number of independent relays; identity is a client-side keypair, and removing content requires every relay carrying it to cooperate.
- [Scuttlebutt](https://www.scuttlebutt.nz/) - Offline-first gossip protocol that replicates signed append-only feeds between mutual follows over LAN or internet; no servers are required, though optional pub and room servers aid discovery.
- [XMPP](https://xmpp.org/) - The Extensible Messaging and Presence Protocol, an open IETF standard for federated messaging with thousands of independently operated servers.

### P2P Networking & Data Transfer
- [BitTorrent](https://www.bittorrent.org/) - The dominant peer-to-peer file-distribution protocol, specified as open BEPs; swarms find each other through trackers or the Mainline DHT.
- [cjdns](https://github.com/cjdelisle/cjdns) - Encrypted IPv6 overlay network with distributed hash table routing.
- [GNUnet](https://gnunet.org/) - A network protocol stack for building secure, distributed, and privacy-preserving applications, with strong roots in academic research.
- [Hypercore Protocol](https://github.com/holepunchto/hypercore) - A fast, scalable, and secure peer-to-peer protocol for everyone (evolution of the [Dat Protocol](https://datproject.org)), now maintained by [Holepunch](https://holepunch.to/) as part of the Pear runtime.
- [IPFS](https://ipfs.tech/) - The InterPlanetary File System, a content-addressed, peer-to-peer protocol for storing and sharing data; content stays retrievable only while some node pins it, and default nodes bootstrap through project-run infrastructure.
- [IPLD](https://ipld.io/) - A content-addressed linked-data model underlying IPFS and related systems.
- [Iroh](https://www.iroh.computer/) - A toolkit for direct peer-to-peer connectivity: QUIC hole-punching, content-addressed blobs and document sync.
- [libp2p](https://libp2p.io/) - A modular peer-to-peer networking stack, the connectivity layer used by IPFS and many other decentralized projects.
- [Named Data Networking](https://named-data.net/) - A content-centric Internet architecture with active research implementations such as NFD.
- [WebRTC](https://www.w3.org/TR/webrtc/) - W3C Recommendation (2021, with companion IETF RFCs) for direct browser-to-browser media and data channels; peers still need an application-provided signaling channel and commonly STUN/TURN servers to establish connections.
- [Yggdrasil](https://yggdrasil-network.github.io/) - An end-to-end encrypted IPv6 overlay network that scales without central coordination.

### Application Frameworks
- [Fedify](https://fedify.dev/) - A TypeScript framework for building federated server applications on ActivityPub.
- [Freenet](https://freenet.org/) - A decentralized, real-time platform for building and running applications entirely on a peer-to-peer network; a ground-up rewrite by the original Freenet founder (the classic Freenet lives on as Hyphanet).
- [Holochain](https://github.com/holochain/holochain) - A peer-to-peer protocol for data sharing and integrity, backed by authoritative hashchains for data provenance.
- [Pear](https://pears.com/) - A peer-to-peer application runtime and deployment system built on Hypercore, by Holepunch.
- [Spritely](https://spritely.institute/) - Distributed object-capability framework (Goblins, OCapN) for building the decentralized social web.
- [Veilid](https://veilid.com/) - An open-source, peer-to-peer, mobile-first networked application framework with strong privacy, by Cult of the Dead Cow.
- [WebXDC](https://webxdc.org/) - A specification for portable web apps that run inside chat messages and sync over any transport, with no server of their own.

### Local-first & CRDTs
- [Automerge](https://automerge.org/) - A CRDT library for building local-first, collaborative applications that sync without a central server.
- [Earthstar](https://github.com/earthstar-project/earthstar) - An offline-first, distributed, syncable, embedded document database for use in peer-to-peer software.
- [m-ld](https://m-ld.org/) - Library enabling consistent, zero latency read and write of shared information, using RDF (JSON-LD) and CRDTs. **Dormant** (no repository activity since 2024-08)
- [p2panda](https://p2panda.org/) - A collection of building blocks for local-first, peer-to-peer applications.
- [Willow](https://willowprotocol.org/) - A protocol for synchronisable, multi-writer data stores, by the authors of Earthstar.
- [Yjs](https://yjs.dev/) - A high-performance CRDT for building collaborative, offline-first applications.

### Mesh & Off-grid Networking
*Listed here for their who-controls-the-network role; the sibling list awesome-resilient-communication covers off-grid operation in depth.*

- [LibreMesh](https://libremesh.org/) - A modular framework for creating OpenWrt/LEDE-based firmwares for wireless mesh nodes.
- [Meshtastic](https://meshtastic.org/) - Open-source, off-grid mesh communication over inexpensive LoRa radios; channel encryption defaults to a well-known shared key, with private channels and public-key direct messages available.
- [Reticulum](https://reticulum.network/) - Cryptography-based networking stack for building resilient networks over almost any medium: LoRa, packet radio, WiFi or TCP/IP. Released under a custom non-OSI license with field-of-use restrictions.

### Identity & Personal Data
- [Decentralized Identifiers](https://www.w3.org/TR/did-core/) - W3C standard for globally unique, cryptographically verifiable identifiers that need no central registry.
- [Decentralized Web Nodes](https://identity.foundation/decentralized-web-node/spec/) - DIF draft specification for personal datastores that sync between a user's own nodes with built-in permissions. **Dormant** (no repository activity since 2024-09)
- [Encrypted Data Vaults](https://identity.foundation/edv-spec/) - A privacy-respecting mechanism for storing, indexing, and retrieving encrypted data at a storage provider.
- [remoteStorage](https://remotestorage.io/) - An open protocol for decoupling data from apps.
- [Solid](https://solidproject.org/) - Specification for personal data pods with app-agnostic access control, based on Linked Data principles; the published protocol is at version 0.10, but real-world deployment remains small.


## Applications
*Things built with decentralized protocols and technologies.*

### Social Networks (Fediverse & beyond)
- [Akkoma](https://akkoma.social/) - Fork of Pleroma, a lightweight federated social networking server on ActivityPub.
- [Bluesky](https://bsky.app/) - Social network built on the AT Protocol; personal data servers are self-hostable, but in practice the network depends on resource-intensive Relay and AppView services that few parties other than Bluesky operate.
- [Bonfire](https://bonfirenetworks.org/) - Modular open-source framework and application for building federated digital spaces.
- [BookWyrm](https://joinbookwyrm.com/) - Federated social reading and book reviews, on ActivityPub.
- [diaspora*](https://diasporafoundation.org/) - Federated social network with its own protocol, organized around aspects (contact groups); one of the oldest running Fediverse projects (2010).
- [Friendica](https://friendi.ca/) - Federated social platform that speaks several protocols at once — ActivityPub, diaspora*, and others — acting as a bridge between networks.
- [GoToSocial](https://gotosocial.org/) - Lightweight ActivityPub social network server.
- [Hubzilla](https://hubzilla.org/) - Federated publishing and social platform built on the Zot protocol, whose nomadic identity lets an account and its data move or mirror between servers.
- [Lemmy](https://join-lemmy.org/) - Federated link aggregator and discussion forum, on ActivityPub.
- [Manyverse](https://www.manyver.se/) - Mobile client for Secure Scuttlebutt, an offline-first gossip protocol that syncs social feeds over LAN or internet; content can be encrypted, but the social graph and metadata are public by design.
- [Mastodon](https://joinmastodon.org/) - Decentralized, federated alternative to Twitter.
- [Mbin](https://joinmbin.org/) - Federated content aggregator and microblogging platform (community fork of /kbin), on ActivityPub.
- [Misskey](https://misskey-hub.net/) - Feature-rich federated microblogging platform on ActivityPub (Sharkey is a popular fork).
- [Mobilizon](https://joinmobilizon.org/) - A federated tool that helps you find, create and organise events.
- [PieFed](https://piefed.social/) - Federated link aggregator and discussion forum with a focus on moderation tooling, on ActivityPub.
- [Pixelfed](https://pixelfed.org/) - Federated photo sharing, on ActivityPub.
- [Pleroma](https://pleroma.social/) - A federated social networking platform.
- [Socialhome](https://socialhome.network/) - Decentralized and federated profile builder with social networking features.

### Media Streaming & Publishing
- [Castopod](https://castopod.org/) - Self-hosted podcast hosting with ActivityPub federation.
- [Funkwhale](https://funkwhale.audio/) - A community-driven project that lets you listen and share music and audio within a decentralized, open network.
- [Mediagoblin](https://mediagoblin.org/) - A free software media publishing platform alternative to Flickr, YouTube, SoundCloud.
- [Owncast](https://owncast.online/) - Self-hosted live video streaming with ActivityPub federation.
- [PeerTube](https://joinpeertube.org/) - Decentralized federated video streaming platform using P2P, ActivityPub and WebTorrent.
- [WriteFreely](https://writefreely.org/) - Minimalist federated blogging platform, on ActivityPub.

### P2P Messaging
- [Berty](https://github.com/berty/berty) - Peer-to-peer messenger over libp2p with Bluetooth LE and local-network proximity transports, requiring no accounts or servers; still beta software.
- [BitMessage](https://wiki.bitmessage.org/) - Encrypted message broadcasting in which every node relays every message, hiding who reads what; the network still runs, but the reference client's last release was in 2018.
- [Briar](https://briarproject.org/) - Messenger that syncs over Tor when the internet works and over Bluetooth or Wi-Fi when it does not; relays only between mutual contacts, not strangers. [Audited by Cure53 (2017)](https://briarproject.org/news/2017-beta-released-security-audit/).
- [Cwtch](https://cwtch.im/) - Metadata-resistant group messenger built on Tor onion services, with untrusted relay servers for offline delivery.
- [Delta Chat](https://delta.chat/) - Decentralized messenger with end-to-end encryption that works over the existing e-mail network.
- [Jami](https://jami.net/) - Distributed peer-to-peer communication (text, voice and video), free and open-source.
- [Retroshare](https://retroshare.cc/) - Establish encrypted connections between you and your friends to create a network of computers, and provides various distributed services: forums, channels, chat, mail.
- [Ricochet Refresh](https://github.com/blueprint-freespeech/ricochet-refresh) - Maintained fork of Ricochet in which every user is a Tor onion service, leaving no server-side metadata; the original was audited by NCC Group (2016), before the v3 onion migration.
- [SimpleX Chat](https://simplex.chat/) - Private messenger without any user identifiers, using decentralized relay servers.
- [Tox](https://tox.chat/) - Serverless peer-to-peer encrypted messaging protocol and implementations (its own documentation notes it has not been independently audited).

### Code & Collaboration
- [Darcs](http://darcs.net/) - Free and open source cross-platform distributed version control system.
- [Forgejo](https://forgejo.org/) - Self-hosted software forge (Gitea fork) implementing ActivityPub-based federation via ForgeFed.
- [Pijul](https://pijul.org/) - A free and open source (GPL2) distributed version control system.
- [Radicle](https://radicle.dev/) - Secure peer-to-peer code collaboration without intermediaries.

### File Storage, Sync and Sharing
- [instant.io](https://instant.io/) - Streaming file transfer over WebTorrent, entirely in the browser with nothing to install.
- [magic-wormhole](https://github.com/magic-wormhole/magic-wormhole) - Transfers files between two computers using short one-time codes over a PAKE-encrypted connection; a public rendezvous server (self-hostable) assists the handshake.
- [OnionShare](https://onionshare.org/) - Hosts the selected files as a hidden service on the user's computer.
- [Peergos](https://peergos.org/) - End-to-end encrypted, peer-to-peer file storage, sharing and communication network.
- [Perkeep](https://perkeep.org/) - Personal, content-addressed storage system designed for lifelong data archiving independent of any provider; development continues at a slow pace.
- [Syncthing](https://syncthing.net/) - Continuous peer-to-peer file synchronization that works fully on a LAN with no internet; relay and discovery servers are optional and self-hostable.
- [Tahoe-LAFS](https://github.com/tahoe-lafs/tahoe-lafs) - A private, encrypted file storage system that decentralizes data across multiple servers.
- [Tribler](https://www.tribler.org) - Privacy enhanced BitTorrent client with P2P content discovery.
- [WebTorrent](https://webtorrent.io/) - An in-browser torrenting that works without requiring users to install anything extra.

### Databases
- [GUN](https://github.com/amark/gun) - Real-time graph database that syncs between JavaScript peers, in practice through relay "super peers"; conflict resolution is eventually consistent, with optional encryption via its SEA module.
- [OrbitDB](https://github.com/orbitdb/orbitdb) - Peer-to-peer database engine of append-only, CRDT-merged logs replicated over IPFS pubsub; eventually consistent, with availability depending on which peers are online.

### Anonymity & Overlay Networks
- [Hidden Lake](https://github.com/number571/hidden-lake) - Anonymous friend-to-friend network built on queue-based messaging, designed to resist traffic analysis even by a global observer.
- [Hyphanet](https://www.hyphanet.org/) - Formerly Freenet, a network aimed at activists and people living in repressive regimes (the new [Freenet](https://freenet.org/) is a separate rewrite by the same founder). It uses a web of trust in high security mode, which makes users on the network very difficult to detect.
- [I2P](https://i2p.net/) - Decentralized garlic-routing overlay for hidden services and peer-to-peer applications; recent academic work documents design weaknesses across its implementations.
- [Tor](https://www.torproject.org/) - Onion-routing anonymity network, the base for onion services and the pluggable-transport ecosystem; repeatedly audited (most recently Cure53, 2023) with a publicly tracked vulnerability history.

### Web, Search and Archiving
- [Agregore](https://agregore.mauve.moe/) - A minimal web browser for the distributed web. Supports IPFS, Hypercore Protocol + more.
- [Cactus Comments](https://cactus.chat/) - A federated comment system for the open web built on Matrix.
- [Ceno Browser](https://censorship.no/) - Censorship-resistant mobile browser that shares and retrieves web content through the Ouinet peer-to-peer cache.
- [IPWB](https://github.com/oduwsdl/ipwb) - An interplanetary wayback machine.
- [yacy](https://github.com/yacy/yacy_search_server) - Distributed Peer-to-Peer Web Search Engine and Intranet Search Appliance.

### Identity & Key Management
- [Dark Crystal](https://darkcrystal.pw/) - Set of protocols, libraries, techniques and guidelines for secure management of sensitive data such as cryptographic keys.
- [Keyoxide](https://keyoxide.org/) - Decentralized, cryptographic identity proofs; a self-hostable Keybase alternative.
- [OpenTimestamps](https://opentimestamps.org/) - A standard format for blockchain timestamping.

## Decentralization at a Glance
A few representative systems — deliberately not all of them — classified on the axes that decide who controls what. Decentralization is not automatically privacy, anonymity, resilience, or censorship resistance: each of those must be designed for separately, and the sibling list awesome-resilient-communication (under *Other Related Lists* below) covers several of them in depth.

|System     |Model                 |User-controlled data|Self-hostable|Offline/LAN|Runs without central relays|Open protocol|Maturity     |
|-----------|----------------------|--------------------|-------------|-----------|---------------------------|-------------|-------------|
|Mastodon   |Federated             |◐                   |✓            |✗          |✓                          |✓ ActivityPub|Mature       |
|Matrix     |Federated             |◐                   |✓            |✗          |◐                          |✓            |Mature       |
|Bluesky    |Federated, hub-heavy  |◐                   |◐            |✗          |✗                          |✓ AT Protocol|Maturing     |
|Nostr      |Relay network         |◐                   |✓            |✗          |◐                          |✓            |Maturing     |
|Delta Chat |Federated (e-mail)    |◐                   |✓            |✗          |◐                          |✓ SMTP/IMAP  |Mature       |
|Scuttlebutt|P2P, local-first      |✓                   |✓            |✓          |✓                          |✓            |Mature, quiet|
|IPFS       |P2P, content-addressed|◐                   |✓            |✓          |◐                          |✓            |Mature       |
|BitTorrent |P2P                   |✓                   |✓            |✓          |◐                          |✓ BEPs       |Mature       |
|Syncthing  |P2P                   |✓                   |✓            |✓          |◐                          |✓            |Mature       |
|Radicle    |P2P                   |✓                   |✓            |◐          |◐                          |✓            |Maturing     |
|Solid      |Federated pods        |✓                   |✓            |✗          |✓                          |✓            |Experimental |

✓ holds by design · ◐ partial or configuration-dependent · ✗ not provided — and in the relay column, ✓ means the system works with no centrally operated helpers at all

<details>
<summary>Why the ◐ cells are conditional (from each project's own documentation)</summary>

- Mastodon and Matrix — your data lives on whichever server hosts your account, so full control means self-hosting; Mastodon migration moves followers but not posts, and Matrix replicates room history to every participating homeserver.
- Matrix relays — nothing in the protocol requires it, but matrix.org remains the default homeserver and identity server for a large share of users.
- Bluesky — personal data servers are practical to self-host, but Relays and AppViews are resource-intensive, so the network in practice depends on a few operators.
- Nostr — identity is a client-side keypair, but notes persist only on the relays that accept them; any relay works and clients publish to several at once, yet some relay is always required.
- Delta Chat — rides on ordinary e-mail, so any provider works, but some provider is always in the loop and sees message metadata.
- Scuttlebutt — feeds replicate between mutual follows over LAN or the internet; optional pub and room servers only aid discovery.
- IPFS — content-addressing removes location trust, but content stays retrievable only while some node pins it, and default configurations bootstrap through project-run nodes.
- BitTorrent and Syncthing — swarms bootstrap through trackers or DHT bootstrap nodes; Syncthing's default discovery and relay servers are project-run but self-hostable, and pure-LAN sync needs neither.
- Radicle — repositories are local Git; sharing them requires seed nodes your peers can reach.
- Solid — the specification is stable on paper (protocol 0.10) but deployments remain small.

</details>

## Choose by Goal
Starting points, not endorsements — the trade-off column is the part to read twice.

|Goal                                      |Starting points                                                                                               |What to keep in mind                                                                                    |
|------------------------------------------|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
|Federated social publishing               |Mastodon or GoToSocial, WriteFreely for blogs, PeerTube for video                                             |You trust your server's operator and moderation; choose the instance as carefully as the software       |
|Private peer-to-peer messaging            |Briar, Cwtch, SimpleX Chat                                                                                    |P2P is not anonymity by itself; match the tool to a threat model first                                  |
|Local-first collaborative applications    |Automerge or Yjs, p2panda, Willow                                                                             |These are libraries and protocols, not products — sync topology and auth are still your design work     |
|Peer-to-peer file transfer and sync       |Syncthing for continuous sync, magic-wormhole for one-shot transfers, WebTorrent in browsers                  |Default discovery and relay servers are project-run; self-host them or stay on LAN for full independence|
|Decentralized code collaboration          |Radicle, Forgejo for federated forges, Darcs or Pijul as the VCS                                              |Radicle needs reachable seed nodes; ForgeFed federation between forges is still early                   |
|Content-addressed publishing              |IPFS, Hypercore/Pear, Iroh                                                                                    |Content stays available only while somebody pins or seeds it                                            |
|Decentralized identity and personal data  |Decentralized Identifiers, Solid, remoteStorage, Keyoxide                                                     |Standards are mature on paper; real-world deployments are small                                         |
|Censorship-resistant or anonymous services|Tor onion services, I2P, Hyphanet, Ceno Browser                                                               |Anonymity is a property of the network and your own practices, not of decentralization                  |
|Building a new decentralized application  |libp2p or Iroh for transport, Automerge or Yjs for data, Spritely or Veilid as frameworks, WebXDC inside chats|Decide early what happens when peers are offline — that choice shapes the whole design                  |

## Graveyard
*Projects that shaped the decentralized web but are no longer maintained. Kept for the historical record. Domains of dead projects are sometimes squatted or hijacked — where that happened, links point to archived copies.*

- [AvionDB](https://github.com/dappkit/aviondb) - Mongodb-like database on top of OrbitDB. **Discontinued**
- [Backfeed](https://github.com/Backfeed/backfeed) - A technology to enable decentralized and user-owned governance and reputation management for a community. **Discontinued**
- [Beaker](https://github.com/beakerbrowser/beaker) - A peer-to-peer Web browser, made for users to run applications independently of hosts. **Discontinued**
- [BigchainDB](https://www.bigchaindb.com/) - A scalable database that layers blockchain technology over decentralized data. **Discontinued**
- [Bit451](https://github.com/Bit451/Bit451) - Decentralized / distributed anonymous peer-to-peer media network. YouTube meets BitTorrent meets Bitcoin. **Discontinued**
- [bitnation](https://web.archive.org/web/2019/https://bitnation.co/) - The World's First Virtual Nation – a Blockchain Jurisdiction. **Discontinued** (domain no longer controlled by the project; link goes to an archived copy).
- [CacheP2P](https://github.com/guerrerocarlos/CacheP2P) - A distributed caching platform. **Discontinued**
- [Cryptosphere](https://github.com/cryptosphere/cryptosphere) - An open-source P2P web application platform for decentralized, privacy-preserving software. **Discontinued**
- [Dat Base](https://github.com/dat-ecosystem-archive/datBase) - Future-friendly apps for your research data pipeline. **Discontinued** (the Dat project wound down).
- [Dat Medium](https://github.com/kewitz/dat-medium) - A markdown blog system for Beaker inspired by Medium. **Discontinued**
- [disaster.radio](https://github.com/sudomesh/disaster-radio) - A disaster-resilient communications network powered by the sun. **Discontinued**
- [ferment](https://web.archive.org/web/2017/https://github.com/fermentation/ferment) - Peer-to-peer audio publishing and streaming application. **Discontinued** (repository deleted).
- [git-ssb](https://github.com/clehner/git-ssb) - Decentralized Git repo hosting and issue tracking on secure-scuttlebutt. **Discontinued** (repository archived in 2018).
- [IPDB](https://ipdb.io/) - A federated database network built on BigchainDB and IPFS. It is maintained by a network of caretakers around the world, at least half of which are nonprofits. **Discontinued**
- [Jolocom](https://web.archive.org/web/2022/https://jolocom.com/) - A decentralised digital identity for everyone. **Discontinued** (domain squatted; link goes to an archived copy).
- [LevelNews](https://web.archive.org/web/2018/https://levelnews.org/) - A leftist news aggregator designed for an open web, and dedicated to journalism without censorship. **Discontinued**
- [libdweb](https://github.com/mozilla/libdweb) - A community effort to implement experimental APIs enabling dweb protocols in Firefox. **Discontinued**
- [Mediachain](https://github.com/mediachain/mediachain) - A media library built on IPFS that makes it easy to publish, track, and discover creative work. **Discontinued** (acquired by Spotify in 2017).
- [Onename](https://onename.com/) - Domain registrar for Blockstack. **Discontinued**
- [OpenBazaar](https://openbazaar.org/) - Marketplace, with store fronts and moderators. **Discontinued** (shut down in 2021).
- [ORC](https://web.archive.org/web/2018/https://orcproject.github.io/) - The Onion Router Cloud, a distributed, anonymous, object storage platform owned and operated by all of us. **Discontinued**
- [Patchwork](https://github.com/ssbc/patchwork) - A decentralized messaging and sharing app built on top of Secure Scuttlebutt. **Discontinued** (repository archived; successor: Manyverse).
- [PeerPad](https://peerpad.net) - A realtime P2P collaborative editing tool, powered by IPFS and CRDTs. **Discontinued**
- [Ricochet](https://ricochet.im/) - Completely anonymous and potentially metadata-free chat **Discontinued**
- [Rotonde](https://wiki.xxiivv.com/site/rotonde.html) - Decentralized social network defined as a shared JSON specification, whose clients ran over the Dat protocol; it faded when the Dat ecosystem wound down. **Discontinued**
- [Samizdat](https://web.archive.org/web/2019/http://samizdat.childrenofmay.org/) - A platform for the self-hosted, peer-to-peer, cryptographically-secured internet. **Discontinued**
- [Shift](https://www.shiftnrg.org) - Decentralized hosting infrastructure for dApps. **Discontinued**
- [StrongLink](https://github.com/btrask/stronglink) - A searchable, syncable, content-addressable notetaking system **Discontinued**
- [Swarm](https://github.com/ethersphere/swarm) - A distributed storage platform and content distribution service of the Ethereum stack; the original Go implementation was archived, but the project remains active through the [Bee](https://github.com/ethersphere/bee) implementation. **Excluded** (modern Swarm depends on BZZ token economics, out of scope for this list; kept here for the historical record).
- [Tahrir](https://github.com/sanity/tahrir) - Encrypted, decentralized Twitter-style microblogging built on a web of trust, by Freenet's founder. **Discontinued**
- [trsst](https://github.com/TrsstProject/trsst) - Encrypted, decentralized Twitter-style microblogging built on syndicated feeds. **Discontinued**
- [Twister](http://twister.net.co/) - A fully decentralized P2P microblogging platform leveraging the free software implementations of Bitcoin and BitTorrent protocols. **Discontinued**
- [Webnative](https://github.com/oddsdk/ts-odd) - JavaScript library that decouples user data from apps and hosts it on IPFS. **Discontinued** (Fission shut down in 2024).
- [Wikipediap2p](https://guerrerocarlos.github.io/WikiP2P.org/) - A peer-to-peer version of Wikipedia. **Discontinued**
- [ZeroNet](https://zeronet.io/) - A peer-to-peer web built on the Bitcoin cryptography for addressing, and identity and Namecoin for .bit domains. **Discontinued** (community fork: [zeronet-conservancy](https://github.com/zeronet-conservancy/zeronet-conservancy)).

## Other Related Lists

- [alternative-internet](https://github.com/redecentralize/alternative-internet) - A collection of interesting new networks and technologies aiming at decentralisation.
- [Awesome-decentralized-id](https://github.com/infominer33/awesome-decentralized-id) - Resources for creating a Decentralized, Vendor Agnostic, Self Sovereign Identity System for people organizations and things.
- [awesome-offline-knowledge](https://github.com/gdamdam/awesome-offline-knowledge) - Content, tools, and infrastructure for keeping knowledge accessible without the internet.
- [awesome-resilient-communication](https://github.com/gdamdam/awesome-resilient-communication) - A curated list of open protocols, applications, hardware, and resources for communication during internet shutdowns, disasters, censorship, and off-grid operation.
- [delightful-fediverse-apps](https://codeberg.org/fediverse/delightful-fediverse-apps) - A curated list of Fediverse applications and services.
## Contributors
- [Contributors](https://github.com/gdamdam/awesome-decentralized-web/graphs/contributors)

This list is released under the [Creative Commons Attribution-ShareAlike 4.0 International License](LICENSE).


