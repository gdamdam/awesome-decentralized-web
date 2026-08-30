# Awesome Decentralized Web [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)


A curated list about the decentralized technologies and tools to develop decentralized applications.
Thanks to the [Decentralized Web Summit](https://web.archive.org/web/2018/https://www.decentralizedweb.net/) for the inspiration.

**Scope.** This list is about the *decentralized web*: peer-to-peer protocols, federated applications, and distributed data — projects where decentralization is the core design, not a feature or a marketing claim.

**Out of scope — submissions will be closed without review:**
- Cryptocurrencies, blockchains, tokens, NFTs, DAOs, DeFi and other finance-related projects. (Merely *using* an existing blockchain as a neutral public record, with no token of its own, can qualify — see the contributing guide below.)
- AI tools, agent frameworks, and "decentralized AI" platforms.
- Commercial products without significant open-source or decentralized relevance.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting a project.

Entries marked **Dormant** still work but have seen no meaningful development for roughly 2 years; dead projects live in the Graveyard section at the bottom.

**A quick taxonomy.** *Federated* systems (Mastodon, Matrix, XMPP) are many independently operated servers interoperating through a shared protocol — you choose which server to trust instead of trusting a central one. *Peer-to-peer* systems (BitTorrent, Scuttlebutt, Tox) exchange data directly between participants without requiring a single authoritative application server — though trackers, bootstrap nodes or relays may assist. *Distributed* only means data or computation is spread across many machines — centralized services can be distributed too; a distributed system is decentralized only when no single party controls it. *Local-first* software (built with Automerge, Yjs or Willow) keeps the authoritative copy of your data on your own device and treats the network as optional, syncing when connectivity allows.

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
  - [Miscellaneous](#miscellaneous)
- [Graveyard](#graveyard)
- [Other Related Lists](#other-related-lists)
- [Contributors](#contributors)


## Protocols and Technologies
*Protocols, stacks and building blocks for a decentralized web.*

### Federation & Social Protocols
- [ActivityPub](https://www.w3.org/TR/activitypub/) - Open, decentralized social networking protocol based on Pump.io's ActivityPump protocol.
- [AT Protocol](https://github.com/bluesky-social/atproto) - The Authenticated Transfer Protocol, an open protocol for decentralized social networking, powering Bluesky.
- [ForgeFed](https://github.com/forgefed/forgefed) - A decentralized federation protocol provides a server to server API for pull request, forking and subscription. **Dormant**
- [Matrix](https://matrix.org/) - An open standard for decentralised persistent communication over IP. Matrix wants to connect together all the various communication services and make them interoperate.
- [Nostr](https://nostr.com/) - A simple, open protocol that enables censorship-resistant, global social networking.
- [Scuttlebutt](https://www.scuttlebutt.nz/) - A decent(ralised), offline-friendly secure gossip protocol. **Dormant**
- [XMPP](https://xmpp.org/) - The Extensible Messaging and Presence Protocol, an open IETF standard for federated messaging with thousands of independently operated servers.

### P2P Networking & Data Transfer
- [BitTorrent](https://en.wikipedia.org/wiki/BitTorrent) - Protocol for distributed file sharing.
- [cjdns](https://github.com/cjdelisle/cjdns) - Encrypted IPv6 overlay network with distributed hash table routing.
- [GNUnet](https://gnunet.org/) - A network protocol stack for building secure, distributed, and privacy-preserving applications, with strong roots in academic research.
- [Hypercore Protocol](https://github.com/holepunchto/hypercore) - A fast, scalable, and secure peer-to-peer protocol for everyone (evolution of the [Dat Protocol](https://datproject.org)), now maintained by [Holepunch](https://holepunch.to/) as part of the Pear runtime.
- [IPFS](https://ipfs.tech/) - The InterPlanetary File System, a content-addressed, peer-to-peer protocol for storing and sharing data.
- [IPLD](https://ipld.io/) - A content-addressed linked-data model underlying IPFS and related systems.
- [Iroh](https://www.iroh.computer/) - A toolkit for direct peer-to-peer connectivity: QUIC hole-punching, content-addressed blobs and document sync.
- [libp2p](https://libp2p.io/) - A modular peer-to-peer networking stack, the connectivity layer used by IPFS and many other decentralized projects.
- [Named Data Networking](https://named-data.net/) - A content-centric Internet architecture with active research implementations such as NFD.
- [WebRTC](https://en.wikipedia.org/wiki/WebRTC) - W3C drafted standard for browser-to-browser data transfer.
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
- [Earthstar](https://github.com/earthstar-project/earthstar) - An offline-first, distributed, syncable, embedded document database for use in peer-to-peer software. **Dormant**
- [m-ld](https://m-ld.org/) - Library enabling consistent, zero latency read and write of shared information, using RDF (JSON-LD) and CRDTs.
- [p2panda](https://p2panda.org/) - A collection of building blocks for local-first, peer-to-peer applications.
- [Willow](https://willowprotocol.org/) - A protocol for synchronisable, multi-writer data stores, by the authors of Earthstar.
- [Yjs](https://yjs.dev/) - A high-performance CRDT for building collaborative, offline-first applications.

### Mesh & Off-grid Networking
- [LibreMesh](https://libremesh.org/) - A modular framework for creating OpenWrt/LEDE-based firmwares for wireless mesh nodes.
- [Meshtastic](https://meshtastic.org/) - Open-source, off-grid mesh communication over inexpensive LoRa radios.
- [Reticulum](https://reticulum.network/) - Cryptography-based networking stack for building resilient networks over almost any medium: LoRa, packet radio, WiFi or TCP/IP.

### Identity & Personal Data
- [Decentralized Identifiers](https://www.w3.org/TR/did-core/) - W3C standard for globally unique, cryptographically verifiable identifiers that need no central registry.
- [Decentralized Web Nodes](https://identity.foundation/decentralized-web-node/spec/) - A mesh-like datastore construction that supports sync, built in permissions, and dynamic interactions between other nodes. **Dormant**
- [Encrypted Data Vaults](https://identity.foundation/edv-spec/) - A privacy-respecting mechanism for storing, indexing, and retrieving encrypted data at a storage provider. **Dormant**
- [remoteStorage](https://remotestorage.io/) - An open protocol for decoupling data from apps.
- [Solid](https://solidproject.org/) - A proposed set of conventions and tools for building decentralized social applications based on Linked Data principles.


## Applications
*Things built with decentralized protocols and technologies.*

### Social Networks (Fediverse & beyond)
- [Akkoma](https://akkoma.social/) - Actively developed fork of Pleroma, a lightweight federated social networking server on ActivityPub.
- [Bluesky](https://bsky.app/) - Decentralized social network built on the AT Protocol, with self-hostable personal data servers.
- [Bonfire](https://bonfirenetworks.org/) - Modular open-source framework and application for building federated digital spaces.
- [BookWyrm](https://joinbookwyrm.com/) - Federated social reading and book reviews, on ActivityPub.
- [diaspora*](https://diasporafoundation.org/) - Decentralized and federated social media platform. **Dormant**
- [Friendica](https://friendi.ca/) - Decentralized and federated social media platform.
- [GoToSocial](https://gotosocial.org/) - Lightweight ActivityPub social network server.
- [Hubzilla](https://hubzilla.org/) - Decentralized and federated social media platform.
- [Lemmy](https://join-lemmy.org/) - Federated link aggregator and discussion forum, on ActivityPub.
- [Manyverse](https://www.manyver.se/) - An iOS and Android mobile app for the decentralized messaging and sharing app built on top of Secure Scuttlebutt. **Dormant**
- [Mastodon](https://joinmastodon.org/) - Decentralized, federated alternative to Twitter.
- [Mbin](https://joinmbin.org/) - Federated content aggregator and microblogging platform (community fork of /kbin), on ActivityPub.
- [Misskey](https://misskey-hub.net/) - Feature-rich federated microblogging platform on ActivityPub (Sharkey is an actively developed fork).
- [Mobilizon](https://joinmobilizon.org/) - A federated tool that helps you find, create and organise events.
- [PieFed](https://piefed.social/) - Federated link aggregator and discussion forum with a focus on moderation tooling, on ActivityPub.
- [Pixelfed](https://pixelfed.org/) - Federated photo sharing, on ActivityPub.
- [Pleroma](https://pleroma.social/) - A federated social networking platform.
- [Socialhome](https://socialhome.network/) - Decentralized and federated profile builder with social networking features. **Dormant**

### Media Streaming & Publishing
- [Castopod](https://castopod.org/) - Self-hosted podcast hosting with ActivityPub federation.
- [Funkwhale](https://funkwhale.audio/) - A community-driven project that lets you listen and share music and audio within a decentralized, open network.
- [Mediagoblin](https://mediagoblin.org/) - A free software media publishing platform alternative to Flickr, YouTube, SoundCloud. **Dormant**
- [Owncast](https://owncast.online/) - Self-hosted live video streaming with ActivityPub federation.
- [PeerTube](https://joinpeertube.org/) - Decentralized federated video streaming platform using P2P, ActivityPub and WebTorrent.
- [WriteFreely](https://writefreely.org/) - Minimalist federated blogging platform, on ActivityPub.

### P2P Messaging
- [Berty](https://github.com/berty/berty) - Anonymous, secure, peer-to-peer protocol that doesn't need an internet connection to function.
- [Briar](https://briarproject.org/) - Peer-to-peer encrypted messaging over Tor, Wi-Fi or Bluetooth, built for activists and journalists.
- [Cwtch](https://cwtch.im/) - Metadata-resistant, decentralized group messaging built on Tor onion services.
- [Delta Chat](https://delta.chat/) - Decentralized messenger with end-to-end encryption that works over the existing e-mail network.
- [Jami](https://jami.net/) - Distributed peer-to-peer communication (text, voice and video), free and open-source.
- [Retroshare](https://retroshare.cc/) - Establish encrypted connections between you and your friends to create a network of computers, and provides various distributed services: forums, channels, chat, mail.
- [Ricochet Refresh](https://github.com/blueprint-freespeech/ricochet-refresh) - New updated version of Ricochet.
- [SimpleX Chat](https://simplex.chat/) - Private messenger without any user identifiers, using decentralized relay servers.
- [Tox](https://tox.chat/) - Serverless peer-to-peer encrypted messaging protocol and implementations (its security model has not received a full independent audit).

### Code & Collaboration
- [Darcs](http://darcs.net/) - Free and open source cross-platform distributed version control system. **Dormant**
- [Forgejo](https://forgejo.org/) - Self-hosted software forge (Gitea fork) implementing ActivityPub-based federation via ForgeFed.
- [Pijul](https://pijul.org/) - A free and open source (GPL2) distributed version control system.
- [Radicle](https://radicle.dev/) - Secure peer-to-peer code collaboration without intermediaries.

### File Storage, Sync and Sharing
- [instant.io](https://instant.io/) - Streaming file transfer over WebTorrent.
- [magic-wormhole](https://github.com/magic-wormhole/magic-wormhole) - Get things from one computer to another, safely.
- [OnionShare](https://onionshare.org/) - Hosts the selected files as a hidden service on the user's computer.
- [Peergos](https://peergos.org/) - End-to-end encrypted, peer-to-peer file storage, sharing and communication network.
- [Perkeep](https://perkeep.org/) - Set of open source formats, protocols, and software for modeling, storing, searching, sharing and synchronizing data.
- [Syncthing](https://syncthing.net/) - Continuous peer-to-peer file synchronization between devices, without any central server.
- [Tahoe-LAFS](https://github.com/tahoe-lafs/tahoe-lafs) - A private, encrypted file storage system that decentralizes data across multiple servers.
- [Tribler](https://www.tribler.org) - Privacy enhanced BitTorrent client with P2P content discovery.
- [WebTorrent](https://webtorrent.io/) - An in-browser torrenting that works without requiring users to install anything extra.

### Databases
- [GUN](https://github.com/amark/gun) - A small, easy, and fast data sync and storage system that runs everywhere JavaScript does. **Dormant**
- [OrbitDB](https://github.com/orbitdb/orbitdb) - Peer-to-peer database engine on top of IPFS.

### Anonymity & Overlay Networks
- [Hidden Lake](https://github.com/number571/hidden-lake) - Anonymous friend-to-friend network built on queue-based messaging, designed to resist traffic analysis even by a global observer.
- [Hyphanet](https://www.hyphanet.org/) - Formerly Freenet, a network aimed at activists and people living in repressive regimes (the new [Freenet](https://freenet.org/) is a separate rewrite by the same founder). It uses a web of trust in high security mode, which makes users on the network very difficult to detect.
- [I2P](https://geti2p.net/) - Anonymous network with hidden services.
- [Tor](https://www.torproject.org/) - Anonymous network proxy.

### Web, Search and Archiving
- [Agregore](https://agregore.mauve.moe/) - A minimal web browser for the distributed web. Supports IPFS, Hypercore Protocol + more.
- [Cactus Comments](https://cactus.chat/) - A federated comment system for the open web built on Matrix. **Dormant**
- [Ceno Browser](https://censorship.no/) - Censorship-resistant mobile browser that shares and retrieves web content through the Ouinet peer-to-peer cache.
- [IPWB](https://github.com/oduwsdl/ipwb) - An interplanetary wayback machine.
- [yacy](https://github.com/yacy/yacy_search_server) - Distributed Peer-to-Peer Web Search Engine and Intranet Search Appliance.

### Identity & Key Management
- [Dark Crystal](https://darkcrystal.pw/) - Set of protocols, libraries, techniques and guidelines for secure management of sensitive data such as cryptographic keys. **Dormant**
- [Keyoxide](https://keyoxide.org/) - Decentralized, cryptographic identity proofs; a self-hostable Keybase alternative.
- [OpenTimestamps](https://opentimestamps.org/) - A standard format for blockchain timestamping.

### Miscellaneous
- [Librem](https://librem.one) - A growing bundle of ethical services by Purism.
- [Rotonde](https://wiki.xxiivv.com/#rotonde) - Commonly agreed upon specifications of a JSON object shared between members of the network. **Dormant**

## Graveyard
*Projects that shaped the decentralized web but are no longer maintained. Kept for the historical record. Domains of dead projects are sometimes squatted or hijacked — where that happened, links point to archived copies.*

- [AvionDB](https://github.com/dappkit/aviondb) - Mongodb-like database on top of OrbitDB. **Discontinued!**
- [Backfeed](https://github.com/Backfeed/backfeed) - A technology to enable decentralized and user-owned governance and reputation management for a community. **Discontinued!**
- [Beaker](https://github.com/beakerbrowser/beaker) - A peer-to-peer Web browser, made for users to run applications independently of hosts. **Discontinued!**
- [BigchainDB](https://www.bigchaindb.com/) - A scalable database that layers blockchain technology over decentralized data. **Discontinued!**
- [Bit451](https://github.com/Bit451/Bit451) - Decentralized / distributed anonymous peer-to-peer media network. YouTube meets BitTorrent meets Bitcoin. **Discontinued!**
- [BitMessage](https://bitmessage.org/wiki/Main_Page) - Anonymous encrypted message broadcasting. **Discontinued!** (unmaintained for years).
- [bitnation](https://web.archive.org/web/2019/https://bitnation.co/) - The World's First Virtual Nation – a Blockchain Jurisdiction. **Discontinued!** (dead; domain now serves unrelated spam, link goes to an archived copy).
- [CacheP2P](https://github.com/guerrerocarlos/CacheP2P) - A distributed caching platform. **Discontinued!**
- [Cryptosphere](https://github.com/cryptosphere/cryptosphere) - An open-source P2P web application platform for decentralized, privacy-preserving software. **Discontinued!**
- [Dat Base](https://github.com/dat-ecosystem-archive/datBase) - Future-friendly apps for your research data pipeline. **Discontinued!** (the Dat project wound down).
- [Dat Medium](https://github.com/kewitz/dat-medium) - A markdown blog system for Beaker inspired by Medium. **Discontinued!**
- [disaster.radio](https://github.com/sudomesh/disaster-radio) - A disaster-resilient communications network powered by the sun. **Discontinued!**
- [ferment](https://web.archive.org/web/2017/https://github.com/fermentation/ferment) - Peer-to-peer audio publishing and streaming application. **Discontinued!** (repository deleted).
- [git-ssb](https://github.com/clehner/git-ssb) - Decentralized Git repo hosting and issue tracking on secure-scuttlebutt. **Discontinued!** (repository archived in 2018).
- [IPDB](https://ipdb.io/) - A federated database network built on BigchainDB and IPFS. It is maintained by a network of caretakers around the world, at least half of which are nonprofits. **Discontinued!**
- [Jolocom](https://web.archive.org/web/2022/https://jolocom.com/) - A decentralised digital identity for everyone. **Discontinued!** (dead; domain squatted, link goes to an archived copy).
- [LevelNews](https://web.archive.org/web/2018/https://levelnews.org/) - A leftist news aggregator designed for an open web, and dedicated to journalism without censorship. **Discontinued!**
- [libdweb](https://github.com/mozilla/libdweb) - A community effort to implement experimental APIs enabling dweb protocols in Firefox. **Discontinued!**
- [Mediachain](https://github.com/mediachain/mediachain) - A media library built on IPFS that makes it easy to publish, track, and discover creative work. **Discontinued!** (acquired by Spotify in 2017).
- [Onename](https://onename.com/) - Domain registar for Blockstack. **Discontinued!**
- [OpenBazaar](https://openbazaar.org/) - Marketplace, with store fronts and moderators. **Discontinued!** (shut down in 2021).
- [ORC](https://web.archive.org/web/2018/https://orcproject.github.io/) - The Onion Router Cloud, a distributed, anonymous, object storage platform owned and operated by all of us. **Discontinued!**
- [Patchwork](https://github.com/ssbc/patchwork) - A decentralized messaging and sharing app built on top of Secure Scuttlebutt. **Discontinued!** (repository archived; successor: Manyverse).
- [PeerPad](https://peerpad.net) - A realtime P2P collaborative editing tool, powered by IPFS and CRDTs. **Discontinued!**
- [Ricochet](https://ricochet.im/) - Completely anonymous and potentially metadata-free chat **Discontinued!**
- [Samizdat](https://web.archive.org/web/2019/http://samizdat.childrenofmay.org/) - A platform for the self-hosted, peer-to-peer, cryptographically-secured internet. **Discontinued!**
- [Shift](https://www.shiftnrg.org) - Decentralized hosting infrastructure for dApps. **Discontinued!**
- [StrongLink](https://github.com/btrask/stronglink) - A searchable, syncable, content-addressable notetaking system **Discontinued!**
- [Swarm](https://github.com/ethersphere/swarm) - A distributed storage platform and content distribution service of the Ethereum stack. **Discontinued!** (repository archived).
- [Tahrir](https://github.com/sanity/tahrir) - Looks and feels like Twitter but encrypted and anonymized and decentralized and only you hold the keys. **Discontinued!**
- [trsst](https://github.com/TrsstProject/trsst) - Looks and feels like Twitter but encrypted and anonymized and decentralized and only you hold the keys. **Discontinued!**
- [Twister](http://twister.net.co/) - A fully decentralized P2P microblogging platform leveraging the free software implementations of Bitcoin and BitTorrent protocols. **Discontinued!**
- [Webnative](https://github.com/oddsdk/ts-odd) - JavaScript library that decouples user data from apps and hosts it on IPFS. **Discontinued!** (Fission shut down in 2024).
- [Wikipediap2p](https://guerrerocarlos.github.io/WikiP2P.org/) - A peer-to-peer version of Wikipedia. **Discontinued!**
- [ZeroNet](https://zeronet.io/) - A peer-to-peer web built on the Bitcoin cryptography for addressing, and identity and Namecoin for .bit domains. **Discontinued!** (community fork: [zeronet-conservancy](https://github.com/zeronet-conservancy/zeronet-conservancy)).

## Other Related Lists

- [alternative-internet](https://github.com/redecentralize/alternative-internet) - A collection of interesting new networks and technologies aiming at decentralisation.
- [Awesome-decentralized-id](https://github.com/infominer33/awesome-decentralized-id) - Resources for creating a Decentralized, Vendor Agnostic, Self Sovereign Identity System for people organizations and things.
- [delightful-fediverse-apps](https://codeberg.org/fediverse/delightful-fediverse-apps) - A curated list of Fediverse applications and services.
## Contributors
- [Contributors](https://github.com/gdamdam/awesome-decentralized-web/graphs/contributors)

This list is released under the [Creative Commons Attribution-ShareAlike 4.0 International License](LICENSE).


