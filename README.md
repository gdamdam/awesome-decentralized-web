# Awesome Decentralized Web [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)


***Status: This repository is in maintenance mode. I no longer actively curate submissions. Critical fixes are welcome, but new additions may take a long time to review.***


A curated list about the decentralized technologies and tools to develop decentralized applications.  
Thanks to the [Decentralized Web Summit](https://www.decentralizedweb.net/) for the inspiration.

***Please do not submit PR with pseudo currencies, blockchain, cryptocoins, NFTs, DAOs and finance related projects.***

***Before submitting:***
- Explain why this project is specifically relevant to decentralized web.
- Do not submit general AI tools.
- Commercial products without significant open-source or decentralized relevance will be closed.


## Protocols and Technologies
*Tools for building a decentralized web.*


### Communication
* [AT Protocol](https://github.com/bluesky-social/atproto) - AT Protocol (Authenticated Transfer Protocol)
* [ForgeFed](https://github.com/forgefed/forgefed) - a decentralized federation protocol provides a server to server API for pull request, forking and subscription.
* [libp2p](https://libp2p.io/) - a modular peer-to-peer networking stack, the connectivity layer used by IPFS and many other decentralized projects.
* [Matrix](https://matrix.org/) - an open standard for decentralised persistent communication over IP. Matrix wants to connect together all the various communication services and make them interoperate.
* [Nostr](https://nostr.com/) -  A decentralized social network with a chance of working. A simple, open protocol that enables a truly censorship-resistant and global social network.
* [Reticulum](https://reticulum.network/) - cryptography-based networking stack for building resilient networks over almost any medium: LoRa, packet radio, WiFi or TCP/IP.
* [Scuttlebutt](https://www.scuttlebutt.nz/) - a decent(ralised), offline-friendly secure gossip protocol.
* [Veilid](https://veilid.com/) - an open-source, peer-to-peer, mobile-first networked application framework with strong privacy, by Cult of the Dead Cow.

### Data
* [Automerge](https://automerge.org/) - a CRDT library for building local-first, collaborative applications that sync without a central server.
* [BitTorrent](https://en.wikipedia.org/wiki/BitTorrent) - protocol for distributed file sharing.
* [Earthstar](https://github.com/earthstar-project/earthstar) - An offline-first, distributed, syncable, embedded document database for use in p2p software.
* [Hypercore Protocol](https://github.com/holepunchto/hypercore) - a fast, scalable, and secure peer-to-peer protocol for everyone (evolution of the [Dat Protocol](https://datproject.org)), now maintained by [Holepunch](https://holepunch.to/) as part of the Pear runtime.
* [Holochain](https://github.com/holochain/holochain) - a peer-to-peer protocol for data sharing and integrity, backed by authoritative hashchains for data provenance.
* [IPFS](https://ipfs.tech/) - or InterPlanetary File System, is a distributed file storage system that aims to replace HTTP.
* [Iroh](https://www.iroh.computer/) - a toolkit for direct peer-to-peer connectivity: QUIC hole-punching, content-addressed blobs and document sync.
* [Willow](https://willowprotocol.org/) - a protocol for synchronisable, multi-writer data stores, by the authors of Earthstar.
* [Yjs](https://yjs.dev/) - a high-performance CRDT for building collaborative, offline-first applications.

### Web
* [ActivityPub](https://www.w3.org/TR/activitypub/) - open, decentralized social networking protocol based on Pump.io's ActivityPump protocol.
* [remoteStorage](https://remotestorage.io/) - An open protocol for decoupling data from apps.
* [Solid](https://solidproject.org/) - a proposed set of conventions and tools for building decentralized social applications based on Linked Data principles.
* [Spritely](https://spritely.institute/) - distributed object-capability framework (Goblins, OCapN) for building the decentralized social web.
* [WebRTC](https://en.wikipedia.org/wiki/WebRTC) - W3C drafted standard for browser-to-browser data transfer.


## Applications
*Things built with decentralized protocols and technologies.*


### Collaboration
* [Forgejo](https://forgejo.org/) - self-hosted software forge (Gitea fork) implementing ActivityPub-based federation via ForgeFed.
* [Radicle](https://radicle.dev/) - secure peer-to-peer code collaboration without intermediaries.
* [Pijul](https://pijul.org/) - Pijul is a free and open source (GPL2) distributed version control system.
* [Darcs](http://darcs.net/) - free and open source X-platform VCS system.

### Communication
* [Berty](https://github.com/berty/berty) - anonymous, secure, peer-to-peer protocol that doesn't need an internet connection to function.
* [Briar](https://briarproject.org/) - peer-to-peer encrypted messaging over Tor, Wi-Fi or Bluetooth, built for activists and journalists.
* [Cwtch](https://cwtch.im/) - metadata-resistant, decentralized group messaging built on Tor onion services.
* [Delta Chat](https://delta.chat/) - decentralized messenger with end-to-end encryption that works over the existing e-mail network.
* [LibreMesh](https://libremesh.org/) - a modular framework for creating OpenWrt/LEDE-based firmwares for wireless mesh nodes.
* [Meshtastic](https://meshtastic.org/) - open-source, off-grid mesh communication over inexpensive LoRa radios.
* [Mobilizon](https://joinmobilizon.org/) -  a federated tool that helps you find, create and organise events.
* [Retroshare](https://retroshare.cc/) -  establish encrypted connections between you and your friends to create a network of computers, and provides various distributed services: forums, channels, chat, mail
* [Ricochet Refresh](https://github.com/blueprint-freespeech/ricochet-refresh) - new updated version of Ricochet
* [SimpleX Chat](https://simplex.chat/) - private messenger without any user identifiers, using decentralized relay servers.
* [Librem](https://librem.one) - Librem One is a growing bundle of ethical services.
* [Jami](https://jami.net/) - Distributed p2p communication(text, voice and video) free and open-source software.

### Databases
* [GUN](https://github.com/amark/gun) - a small, easy, and fast data sync and storage system that runs everywhere JavaScript does.
* [OrbitDB](https://github.com/orbitdb/orbit-db) - p2p database engine on top of IPFS.

### Data Storage and Sharing
* [Decentralized Web Nodes](https://identity.foundation/decentralized-web-node/spec/) - a mesh-like datastore construction that supports sync, built in permissions, and dynamic interactions between other nodes.
* [Encrypted Data Vaults](https://identity.foundation/edv-spec/) - a privacy-respecting mechanism for storing, indexing, and retrieving encrypted data at a storage provider. 
* [instant.io](https://instant.io/) - streaming file transfer over WebTorrent.
* [m-ld](https://m-ld.org/) - Library enabling consistent, zero latency read and write of shared information, using RDF (JSON-LD) and CRDTs.
* [OnionShare](https://onionshare.org/) - hosts the selected files as a hidden service on the user's computer
* [Peergos](https://peergos.org/) - end-to-end encrypted, peer-to-peer file storage, sharing and communication network.
* [Perkeep](https://perkeep.org/) - set of open source formats, protocols, and software for modeling, storing, searching, sharing and synchronizing data.
* [Rotonde](https://wiki.xxiivv.com/#rotonde) - commonly agreed upon specifications of a JSON object shared between members of the network.
* [Tahoe-LAFS](https://www.tahoe-lafs.org/trac/tahoe-lafs) - a private, encrypted file storage system that decentralizes data across multiple servers.
* [Tribler](https://www.tribler.org) - Privacy enhanced BitTorrent client with P2P content discovery.
* [Syncthing](https://syncthing.net/) - continuous peer-to-peer file synchronization between devices, without any central server.
* [WebTorrent](https://webtorrent.io/) - an in-browser torrenting that works without requiring users to install anything extra.

### Media
* [Mediagoblin](https://mediagoblin.org/) - a free software media publishing platform alternative to Flickr, YouTube, SoundCloud.
* [Owncast](https://owncast.online/) - self-hosted live video streaming with ActivityPub federation.
* [PeerTube](https://joinpeertube.org/) - Decentralized federated video streaming platform using P2P, ActivityPub and WebTorrent.
* [Funkwhale](https://funkwhale.audio/) - Funkwhale is a community-driven project that lets you listen and share music and audio within a decentralized, open network.

### Microblogging and Social Network
* [Bluesky](https://bsky.app/) - decentralized social network built on the AT Protocol, with self-hostable personal data servers.
* [BookWyrm](https://joinbookwyrm.com/) - federated social reading and book reviews, on ActivityPub.
* [diaspora*](https://diasporafoundation.org/) - decentralized and federated social media platform.
* [Friendica](https://friendi.ca/) - decentralized and federated social media platform.
* [GoToSocial](https://gotosocial.org/) - lightweight ActivityPub social network server.
* [Hubzilla](https://hubzilla.org/) - decentralized and federated social media platform.
* [Lemmy](https://join-lemmy.org/) - federated link aggregator and discussion forum, on ActivityPub.
* [Mastodon](https://mastodon.social) - decentralized alternative to twitter, with servers federation.
* [Manyverse](https://www.manyver.se/) - An iOS and Android mobile app for the decentralized messaging and sharing app built on top of Secure Scuttlebutt
* [Pixelfed](https://pixelfed.org/) - federated photo sharing, on ActivityPub.
* [Pleroma](https://pleroma.social/) - a federated social networking platform.
* [Socialhome](https://socialhome.network/) - decentralized and federated profile builder with social networking features.

### Miscellaneous
* [Keyoxide](https://keyoxide.org/) - decentralized, cryptographic identity proofs; a self-hostable Keybase alternative.
* [magic-wormhole](https://github.com/warner/magic-wormhole) - get things from one computer to another, safely.
* [OpenTimeStamps](https://opentimestamps.org/) - OpenTimestamps aims to be a standard format for blockchain timestamping.
* [Dark Crystal](https://darkcrystal.pw/) - set of protocols, libraries, techniques and guidelines for secure management of sensitive data such as cryptographic keys.

### Web
* [Agregore](https://agregore.mauve.moe/) - A minimal web browser for the distributed web. Supports IPFS, Hypercore Protocol + more.
* [Cactus Comments](https://cactus.chat/) - Cactus Comments is a federated comment system for the open web built on Matrix.
* [Hyphanet](https://www.hyphanet.org/) - formerly Freenet, a network aimed at activists and people living in repressive regimes (the new [Freenet](https://freenet.org/) is a separate rewrite by the same founder). It uses a web of trust in high security mode, which allows users on the network to be effectively undetectable.
* [GNUnet](https://gnunet.org/) - GNUnet is a new network protocol stack for building secure, distributed, and privacy-preserving applications. With strong roots in academic research, our goal is to replace the old insecure Internet protocol stack.
* [I2P](https://geti2p.net/) - anonymous network with hidden services.
* [IPWB](https://github.com/oduwsdl/ipwb) - an interplanetary wayback machine.
* [Session](https://getsession.org/) - onion-routed private messenger that minimizes metadata (formerly the Loki project).
* [Autonomi](https://autonomi.com/) - decentralized internet and app infrastructure which rewards users for participating in the network (formerly MaidSafe / SAFE Network).
* [Tor](https://www.torproject.org/) - anonymous network proxy.
* [yacy](https://github.com/yacy/yacy_search_server) - Distributed Peer-to-Peer Web Search Engine and Intranet Search Appliance.


## Graveyard
*Projects that shaped the decentralized web but are no longer maintained. Kept for the historical record. Domains of dead projects are sometimes squatted or hijacked — where that happened, links point to archived copies.*

* [AvionDB](https://github.com/dappkit/aviondb) - mongodb-like database on top of OrbitDB. **Discontinued!**
* [Backfeed](http://backfeed.cc/) - a technology to enable decentralized and user-owned governance and reputation management for a community. **Discontinued!**
* [Beaker](https://github.com/beakerbrowser/beaker) - Beaker is a peer-to-peer Web browser, made for users to run applications independently of hosts. **Discontinued!**
* [BigchainDB](https://www.bigchaindb.com/) - a scalable database that layers blockchain technology over decentralized data. **Discontinued!**
* [Bit451](https://github.com/Bit451/Bit451) - decentralized / distributed anonymous p2p media network. YouTube meets BitTorrent meets Bitcoin. **Discontinued!**
* [BitMessage](https://bitmessage.org/wiki/Main_Page) - anonymous encrypted message broadcasting. **Discontinued!** (unmaintained for years)
* bitnation ([archived site](https://web.archive.org/web/2019/https://bitnation.co/)) - the World's First Virtual Nation – A Blockchain Jurisdiction. **Discontinued!** (domain now serves unrelated spam)
* [CacheP2P](https://github.com/guerrerocarlos/CacheP2P) - a distributed caching platform. **Discontinued!**
* [Cryptosphere](https://cryptosphere.io/) - an open-source P2P web application platform for decentralized, privacy-preserving software. **Discontinued!**
* [Dat Base](https://datbase.org) - future-friendly apps for your research data pipeline. **Discontinued!** (the Dat project wound down)
* [Dat Medium](https://github.com/kewitz/dat-medium) - Dat Medium is markdown blog system for Beaker inspired by Medium. **Discontinued!**
* [disaster.radio](https://disaster.radio) - a disaster-resilient communications network powered by the sun. **Discontinued!**
* [ferment](https://github.com/fermentation/ferment) - Peer-to-peer audio publishing and streaming application. **Discontinued!** (repository deleted)
* [git-ssb](https://github.com/clehner/git-ssb) - Decentralized git repo hosting and issue tracking on secure-scuttlebutt. **Discontinued!** (repository archived in 2018)
* [IPDB](https://ipdb.io/) - a federated database network built on BigchainDB and IPFS. It is maintained by a network of caretakers around the world, at least half of which are nonprofits. **Discontinued!**
* Jolocom ([archived site](https://web.archive.org/web/2022/https://jolocom.com/)) - a decentralised digital identity for everyone. **Discontinued!** (domain squatted)
* [LevelNews](https://levelnews.org/) - a leftist news aggregator designed for an open web, and dedicated to journalism without censorship. **Discontinued!**
* [libdweb](https://github.com/mozilla/libdweb) - a community effort to implement experimental APIs enabling dweb protocols in Firefox. **Discontinued!**
* [Mediachain](http://www.mediachain.io/) -  a media library built on IPFS that makes it easy to publish, track, and discover creative work. **Discontinued!** (acquired by Spotify in 2017)
* [Onename](https://onename.com/) - domain registar for Blockstack. **Discontinued!**
* [OpenBazaar](https://openbazaar.org/) - marketplace, with store fronts and moderators. **Discontinued!** (shut down in 2021)
* [ORC](https://orcproject.github.io/) - the Onion Router Cloud, a distributed, anonymous, object storage platform owned and operated by all of us. **Discontinued!**
* [Patchwork](https://github.com/ssbc/patchwork) - a decentralized messaging and sharing app built on top of Secure Scuttlebutt. **Discontinued!** (repository archived; successor: Manyverse)
* [PeerPad](https://peerpad.net) - a realtime P2P collaborative editing tool, powered by IPFS and CRDTs. **Discontinued!**
* [Ricochet](https://ricochet.im/) - completely anonymous and potentially metadata-free chat **Discontinued!**
* [Samizdat](http://samizdat.childrenofmay.org/) - Samizdat is a platform for the self-hosted, peer-to-peer, cryptographically-secured internet. **Discontinued!**
* [Shift](https://www.shiftnrg.org) - Decentralized hosting infrastructure for dApps. **Discontinued!**
* [StrongLink](https://github.com/btrask/stronglink) - a searchable, syncable, content-addressable notetaking system **Discontinued!**
* [Swarm](https://github.com/ethersphere/swarm) - a distributed storage platform and content distribution service of the ethereum stack. **Discontinued!** (repository archived)
* [Tahrir](http://tahrirproject.org/) - looks and feels like twitter but encrypted and anonymized and decentralized and only you hold the keys. **Discontinued!**
* [trsst](https://github.com/TrsstProject/trsst) - looks and feels like twitter but encrypted and anonymized and decentralized and only you hold the keys. **Discontinued!**
* [Twister](http://twister.net.co/) - a fully decentralized P2P microblogging platform leveraging the free software implementations of Bitcoin and BitTorrent protocols. **Discontinued!**
* [Webnative](https://fission.codes/) - JavaScript library that decouples user data from apps and hosts it on IPFS. **Discontinued!** (Fission shut down in 2024)
* [Wikipediap2p](https://guerrerocarlos.github.io/WikiP2P.org/) - a p2p version of wikipedia. **Discontinued!**
* [ZeroNet](https://zeronet.io/) - a peer-to-peer web built on the Bitcoin cryptography for addressing, and identity and Namecoin for .bit domains. **Discontinued!** (community fork: [zeronet-conservancy](https://github.com/zeronet-conservancy/zeronet-conservancy))

## Other Related Lists
* [Awesome-decentralized-id](https://github.com/infominer33/awesome-decentralized-id) - Resources for creating a Decentralized, Vendor Agnostic, Self Sovereign Identity System for people organizations and things.

## Contributors
- [Contributors](https://github.com/gdamdam/awesome-decentralized-web/graphs/contributors)


## License
 [![CC4](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-sa/4.0/)
