# Awesome Decentralized Web [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)


A curated list about the decentralized technologies and tools to develop decentralized applications.
Thanks to the [Decentralized Web Summit](https://www.decentralizedweb.net/) for the inspiration.

**Scope.** This list is about the *decentralized web*: peer-to-peer protocols, federated applications, and distributed data — projects where decentralization is the core design, not a feature or a marketing claim.

**Out of scope — submissions will be closed without review:**
- Cryptocurrencies, blockchains, tokens, NFTs, DAOs, DeFi and other finance-related projects.
- AI tools, agent frameworks, and "decentralized AI" platforms.
- Commercial products without significant open-source or decentralized relevance.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting a project.


## Protocols and Technologies
*Protocols, stacks and building blocks for a decentralized web.*

### Federation & Social Protocols
- [ActivityPub](https://www.w3.org/TR/activitypub/) - Open, decentralized social networking protocol based on Pump.io's ActivityPump protocol.
- [AT Protocol](https://github.com/bluesky-social/atproto) - The Authenticated Transfer Protocol, an open protocol for decentralized social networking, powering Bluesky.
- [ForgeFed](https://github.com/forgefed/forgefed) - A decentralized federation protocol provides a server to server API for pull request, forking and subscription.
- [Matrix](https://matrix.org/) - An open standard for decentralised persistent communication over IP. Matrix wants to connect together all the various communication services and make them interoperate.
- [Nostr](https://nostr.com/) - A decentralized social network with a chance of working. A simple, open protocol that enables a truly censorship-resistant and global social network.
- [Scuttlebutt](https://www.scuttlebutt.nz/) - A decent(ralised), offline-friendly secure gossip protocol.

### P2P Networking & Data Transfer
- [BitTorrent](https://en.wikipedia.org/wiki/BitTorrent) - Protocol for distributed file sharing.
- [GNUnet](https://gnunet.org/) - A network protocol stack for building secure, distributed, and privacy-preserving applications, with strong roots in academic research.
- [Hypercore Protocol](https://github.com/holepunchto/hypercore) - A fast, scalable, and secure peer-to-peer protocol for everyone (evolution of the [Dat Protocol](https://datproject.org)), now maintained by [Holepunch](https://holepunch.to/) as part of the Pear runtime.
- [IPFS](https://ipfs.tech/) - The InterPlanetary File System, a distributed file storage system that aims to replace HTTP.
- [Iroh](https://www.iroh.computer/) - A toolkit for direct peer-to-peer connectivity: QUIC hole-punching, content-addressed blobs and document sync.
- [libp2p](https://libp2p.io/) - A modular peer-to-peer networking stack, the connectivity layer used by IPFS and many other decentralized projects.
- [WebRTC](https://en.wikipedia.org/wiki/WebRTC) - W3C drafted standard for browser-to-browser data transfer.

### Application Frameworks
- [Holochain](https://github.com/holochain/holochain) - A peer-to-peer protocol for data sharing and integrity, backed by authoritative hashchains for data provenance.
- [Spritely](https://spritely.institute/) - Distributed object-capability framework (Goblins, OCapN) for building the decentralized social web.
- [Veilid](https://veilid.com/) - An open-source, peer-to-peer, mobile-first networked application framework with strong privacy, by Cult of the Dead Cow.

### Local-first & CRDTs
- [Automerge](https://automerge.org/) - A CRDT library for building local-first, collaborative applications that sync without a central server.
- [Earthstar](https://github.com/earthstar-project/earthstar) - An offline-first, distributed, syncable, embedded document database for use in p2p software.
- [m-ld](https://m-ld.org/) - Library enabling consistent, zero latency read and write of shared information, using RDF (JSON-LD) and CRDTs.
- [Willow](https://willowprotocol.org/) - A protocol for synchronisable, multi-writer data stores, by the authors of Earthstar.
- [Yjs](https://yjs.dev/) - A high-performance CRDT for building collaborative, offline-first applications.

### Mesh & Off-grid Networking
- [LibreMesh](https://libremesh.org/) - A modular framework for creating OpenWrt/LEDE-based firmwares for wireless mesh nodes.
- [Meshtastic](https://meshtastic.org/) - Open-source, off-grid mesh communication over inexpensive LoRa radios.
- [Reticulum](https://reticulum.network/) - Cryptography-based networking stack for building resilient networks over almost any medium: LoRa, packet radio, WiFi or TCP/IP.

### Identity & Personal Data
- [Decentralized Web Nodes](https://identity.foundation/decentralized-web-node/spec/) - A mesh-like datastore construction that supports sync, built in permissions, and dynamic interactions between other nodes.
- [Encrypted Data Vaults](https://identity.foundation/edv-spec/) - A privacy-respecting mechanism for storing, indexing, and retrieving encrypted data at a storage provider.
- [remoteStorage](https://remotestorage.io/) - An open protocol for decoupling data from apps.
- [Solid](https://solidproject.org/) - A proposed set of conventions and tools for building decentralized social applications based on Linked Data principles.


## Applications
*Things built with decentralized protocols and technologies.*

### Social Networks (Fediverse & beyond)
- [Bluesky](https://bsky.app/) - Decentralized social network built on the AT Protocol, with self-hostable personal data servers.
- [BookWyrm](https://joinbookwyrm.com/) - Federated social reading and book reviews, on ActivityPub.
- [diaspora*](https://diasporafoundation.org/) - Decentralized and federated social media platform.
- [Friendica](https://friendi.ca/) - Decentralized and federated social media platform.
- [GoToSocial](https://gotosocial.org/) - Lightweight ActivityPub social network server.
- [Hubzilla](https://hubzilla.org/) - Decentralized and federated social media platform.
- [Lemmy](https://join-lemmy.org/) - Federated link aggregator and discussion forum, on ActivityPub.
- [Manyverse](https://www.manyver.se/) - An iOS and Android mobile app for the decentralized messaging and sharing app built on top of Secure Scuttlebutt.
- [Mastodon](https://mastodon.social) - Decentralized alternative to twitter, with servers federation.
- [Mobilizon](https://joinmobilizon.org/) - A federated tool that helps you find, create and organise events.
- [Pixelfed](https://pixelfed.org/) - Federated photo sharing, on ActivityPub.
- [Pleroma](https://pleroma.social/) - A federated social networking platform.
- [Socialhome](https://socialhome.network/) - Decentralized and federated profile builder with social networking features.

### Media Streaming & Publishing
- [Funkwhale](https://funkwhale.audio/) - A community-driven project that lets you listen and share music and audio within a decentralized, open network.
- [Mediagoblin](https://mediagoblin.org/) - A free software media publishing platform alternative to Flickr, YouTube, SoundCloud.
- [Owncast](https://owncast.online/) - Self-hosted live video streaming with ActivityPub federation.
- [PeerTube](https://joinpeertube.org/) - Decentralized federated video streaming platform using P2P, ActivityPub and WebTorrent.

### P2P Messaging
- [Berty](https://github.com/berty/berty) - Anonymous, secure, peer-to-peer protocol that doesn't need an internet connection to function.
- [Briar](https://briarproject.org/) - Peer-to-peer encrypted messaging over Tor, Wi-Fi or Bluetooth, built for activists and journalists.
- [Cwtch](https://cwtch.im/) - Metadata-resistant, decentralized group messaging built on Tor onion services.
- [Delta Chat](https://delta.chat/) - Decentralized messenger with end-to-end encryption that works over the existing e-mail network.
- [Jami](https://jami.net/) - Distributed p2p communication(text, voice and video) free and open-source software.
- [Retroshare](https://retroshare.cc/) - Establish encrypted connections between you and your friends to create a network of computers, and provides various distributed services: forums, channels, chat, mail.
- [Ricochet Refresh](https://github.com/blueprint-freespeech/ricochet-refresh) - New updated version of Ricochet.
- [SimpleX Chat](https://simplex.chat/) - Private messenger without any user identifiers, using decentralized relay servers.

### Code & Collaboration
- [Darcs](http://darcs.net/) - Free and open source X-platform VCS system.
- [Forgejo](https://forgejo.org/) - Self-hosted software forge (Gitea fork) implementing ActivityPub-based federation via ForgeFed.
- [Pijul](https://pijul.org/) - A free and open source (GPL2) distributed version control system.
- [Radicle](https://radicle.dev/) - Secure peer-to-peer code collaboration without intermediaries.

### File Storage, Sync and Sharing
- [instant.io](https://instant.io/) - Streaming file transfer over WebTorrent.
- [magic-wormhole](https://github.com/warner/magic-wormhole) - Get things from one computer to another, safely.
- [OnionShare](https://onionshare.org/) - Hosts the selected files as a hidden service on the user's computer.
- [Peergos](https://peergos.org/) - End-to-end encrypted, peer-to-peer file storage, sharing and communication network.
- [Perkeep](https://perkeep.org/) - Set of open source formats, protocols, and software for modeling, storing, searching, sharing and synchronizing data.
- [Syncthing](https://syncthing.net/) - Continuous peer-to-peer file synchronization between devices, without any central server.
- [Tahoe-LAFS](https://www.tahoe-lafs.org/trac/tahoe-lafs) - A private, encrypted file storage system that decentralizes data across multiple servers.
- [Tribler](https://www.tribler.org) - Privacy enhanced BitTorrent client with P2P content discovery.
- [WebTorrent](https://webtorrent.io/) - An in-browser torrenting that works without requiring users to install anything extra.

### Databases
- [GUN](https://github.com/amark/gun) - A small, easy, and fast data sync and storage system that runs everywhere JavaScript does.
- [OrbitDB](https://github.com/orbitdb/orbit-db) - P2p database engine on top of IPFS.

### Anonymity & Overlay Networks
- [Hyphanet](https://www.hyphanet.org/) - Formerly Freenet, a network aimed at activists and people living in repressive regimes (the new [Freenet](https://freenet.org/) is a separate rewrite by the same founder). It uses a web of trust in high security mode, which allows users on the network to be effectively undetectable.
- [I2P](https://geti2p.net/) - Anonymous network with hidden services.
- [Tor](https://www.torproject.org/) - Anonymous network proxy.

### Web, Search and Archiving
- [Agregore](https://agregore.mauve.moe/) - A minimal web browser for the distributed web. Supports IPFS, Hypercore Protocol + more.
- [Cactus Comments](https://cactus.chat/) - A federated comment system for the open web built on Matrix.
- [IPWB](https://github.com/oduwsdl/ipwb) - An interplanetary wayback machine.
- [yacy](https://github.com/yacy/yacy_search_server) - Distributed Peer-to-Peer Web Search Engine and Intranet Search Appliance.

### Identity & Key Management
- [Dark Crystal](https://darkcrystal.pw/) - Set of protocols, libraries, techniques and guidelines for secure management of sensitive data such as cryptographic keys.
- [Keyoxide](https://keyoxide.org/) - Decentralized, cryptographic identity proofs; a self-hostable Keybase alternative.
- [OpenTimeStamps](https://opentimestamps.org/) - A standard format for Blockchain timestamping.

### Miscellaneous
- [Librem](https://librem.one) - A growing bundle of ethical services by Purism.
- [Rotonde](https://wiki.xxiivv.com/#rotonde) - Commonly agreed upon specifications of a JSON object shared between members of the network.

## Graveyard
*Projects that shaped the decentralized web but are no longer maintained. Kept for the historical record. Domains of dead projects are sometimes squatted or hijacked — where that happened, links point to archived copies.*

- [AvionDB](https://github.com/dappkit/aviondb) - Mongodb-like database on top of OrbitDB. **Discontinued!**
- [Backfeed](http://backfeed.cc/) - A technology to enable decentralized and user-owned governance and reputation management for a community. **Discontinued!**
- [Beaker](https://github.com/beakerbrowser/beaker) - A peer-to-peer Web browser, made for users to run applications independently of hosts. **Discontinued!**
- [BigchainDB](https://www.bigchaindb.com/) - A scalable database that layers Blockchain technology over decentralized data. **Discontinued!**
- [Bit451](https://github.com/Bit451/Bit451) - Decentralized / distributed anonymous p2p media network. YouTube meets BitTorrent meets Bitcoin. **Discontinued!**
- [BitMessage](https://bitmessage.org/wiki/Main_Page) - Anonymous encrypted message broadcasting. **Discontinued!** (unmaintained for years).
- [bitnation](https://web.archive.org/web/2019/https://bitnation.co/) - The World's First Virtual Nation – a Blockchain Jurisdiction. **Discontinued!** (dead; domain now serves unrelated spam, link goes to an archived copy).
- [CacheP2P](https://github.com/guerrerocarlos/CacheP2P) - A distributed caching platform. **Discontinued!**
- [Cryptosphere](https://cryptosphere.io/) - An open-source P2P web application platform for decentralized, privacy-preserving software. **Discontinued!**
- [Dat Base](https://datbase.org) - Future-friendly apps for your research data pipeline. **Discontinued!** (the Dat project wound down).
- [Dat Medium](https://github.com/kewitz/dat-medium) - A markdown blog system for Beaker inspired by Medium. **Discontinued!**
- [disaster.radio](https://disaster.radio) - A disaster-resilient communications network powered by the sun. **Discontinued!**
- [ferment](https://github.com/fermentation/ferment) - Peer-to-peer audio publishing and streaming application. **Discontinued!** (repository deleted).
- [git-ssb](https://github.com/clehner/git-ssb) - Decentralized Git repo hosting and issue tracking on secure-scuttlebutt. **Discontinued!** (repository archived in 2018).
- [IPDB](https://ipdb.io/) - A federated database network built on BigchainDB and IPFS. It is maintained by a network of caretakers around the world, at least half of which are nonprofits. **Discontinued!**
- [Jolocom](https://web.archive.org/web/2022/https://jolocom.com/) - A decentralised digital identity for everyone. **Discontinued!** (dead; domain squatted, link goes to an archived copy).
- [LevelNews](https://levelnews.org/) - A leftist news aggregator designed for an open web, and dedicated to journalism without censorship. **Discontinued!**
- [libdweb](https://github.com/mozilla/libdweb) - A community effort to implement experimental APIs enabling dweb protocols in Firefox. **Discontinued!**
- [Mediachain](http://www.mediachain.io/) - A media library built on IPFS that makes it easy to publish, track, and discover creative work. **Discontinued!** (acquired by Spotify in 2017).
- [Onename](https://onename.com/) - Domain registar for Blockstack. **Discontinued!**
- [OpenBazaar](https://openbazaar.org/) - Marketplace, with store fronts and moderators. **Discontinued!** (shut down in 2021).
- [ORC](https://orcproject.github.io/) - The Onion Router Cloud, a distributed, anonymous, object storage platform owned and operated by all of us. **Discontinued!**
- [Patchwork](https://github.com/ssbc/patchwork) - A decentralized messaging and sharing app built on top of Secure Scuttlebutt. **Discontinued!** (repository archived; successor: Manyverse).
- [PeerPad](https://peerpad.net) - A realtime P2P collaborative editing tool, powered by IPFS and CRDTs. **Discontinued!**
- [Ricochet](https://ricochet.im/) - Completely anonymous and potentially metadata-free chat **Discontinued!**
- [Samizdat](http://samizdat.childrenofmay.org/) - A platform for the self-hosted, peer-to-peer, cryptographically-secured internet. **Discontinued!**
- [Shift](https://www.shiftnrg.org) - Decentralized hosting infrastructure for dApps. **Discontinued!**
- [StrongLink](https://github.com/btrask/stronglink) - A searchable, syncable, content-addressable notetaking system **Discontinued!**
- [Swarm](https://github.com/ethersphere/swarm) - A distributed storage platform and content distribution service of the Ethereum stack. **Discontinued!** (repository archived).
- [Tahrir](http://tahrirproject.org/) - Looks and feels like twitter but encrypted and anonymized and decentralized and only you hold the keys. **Discontinued!**
- [trsst](https://github.com/TrsstProject/trsst) - Looks and feels like twitter but encrypted and anonymized and decentralized and only you hold the keys. **Discontinued!**
- [Twister](http://twister.net.co/) - A fully decentralized P2P microblogging platform leveraging the free software implementations of Bitcoin and BitTorrent protocols. **Discontinued!**
- [Webnative](https://fission.codes/) - JavaScript library that decouples user data from apps and hosts it on IPFS. **Discontinued!** (Fission shut down in 2024).
- [Wikipediap2p](https://guerrerocarlos.github.io/WikiP2P.org/) - A p2p version of wikipedia. **Discontinued!**
- [ZeroNet](https://zeronet.io/) - A peer-to-peer web built on the Bitcoin cryptography for addressing, and identity and Namecoin for .bit domains. **Discontinued!** (community fork: [zeronet-conservancy](https://github.com/zeronet-conservancy/zeronet-conservancy)).

## Other Related Lists
- [Awesome-decentralized-id](https://github.com/infominer33/awesome-decentralized-id) - Resources for creating a Decentralized, Vendor Agnostic, Self Sovereign Identity System for people organizations and things.

## Contributors
- [Contributors](https://github.com/gdamdam/awesome-decentralized-web/graphs/contributors)


