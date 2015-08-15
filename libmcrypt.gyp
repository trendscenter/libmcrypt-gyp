{
    'targets': [
        {
            'target_name': 'libmcrypt',
            'type': 'static_library',
            'msvs_guid': '6a12df1b-cf7c-4a5d-a7e5-e74c8fd7f863',
            'defines': [
                'HAVE_CONFIG_H',
                'LIBDIR="modules/algorithms/:modules/modes/"'
            ],
            'include_dirs': [
                '.',
                'lib/',
                'include/'
            ],
            'sources': [
                'modules/algorithms/3-way.c',
                'modules/algorithms/arcfour.c',
                'modules/algorithms/blowfish.c',
                'modules/algorithms/blowfish-compat.c',
                'modules/algorithms/cast-128.c',
                'modules/algorithms/cast-256.c',
                'modules/algorithms/des.c',
                'modules/algorithms/enigma.c',
                'modules/algorithms/gost.c',
                'modules/algorithms/loki97.c',
                'modules/algorithms/panama.c',
                'modules/algorithms/rc2.c',
                'modules/algorithms/rijndael-128.c',
                'modules/algorithms/rijndael-192.c',
                'modules/algorithms/rijndael-256.c',
                'modules/algorithms/safer64.c',
                'modules/algorithms/safer128.c',
                'modules/algorithms/saferplus.c',
                'modules/algorithms/serpent.c',
                'modules/algorithms/tripledes.c',
                'modules/algorithms/twofish.c',
                'modules/algorithms/wake.c',
                'modules/algorithms/xtea.c',
                'modules/modes/cbc.c',
                'modules/modes/cfb.c',
                'modules/modes/ctr.c',
                'modules/modes/ecb.c',
                'modules/modes/ncfb.c',
                'modules/modes/nofb.c',
                'modules/modes/ofb.c',
                'modules/modes/stream.c',
                'lib/bzero.c', 
                'lib/mcrypt.c', 
                'lib/mcrypt_extra.c', 
                'lib/mcrypt_modules.c', 
                'lib/mcrypt_symb.c', 
                'lib/mcrypt_threads.c', 
                'lib/win32_comp.c', 
                'lib/xmemory.c'
            ]
        }
    ]
}