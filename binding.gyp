{
	'targets' : [
		{
			'target_name': 'scrypt_lib',
			'type': '<(library)',
			'defines': [ #This config file is custom generated for each POSIX OS
				'CONFIG_H_FILE="../config.h"',
			],
			'include_dirs' : [
				'scrypt-1.1.6',
				'scrypt-1.1.6/lib/util',
				#'scrypt-1.1.6/lib/crypto',
			],
			'sources': [
				#'scrypt-1.1.6/lib/scryptenc/scryptenc.c',
				#'scrypt-1.1.6/lib/util/memlimit.c',
				#'scrypt-1.1.6/lib/scryptenc/scryptenc_cpuperf.c',
				#'scrypt-1.1.6/lib/crypto/sha256.c',
				#'scrypt-1.1.6/lib/crypto/crypto_aesctr.c',
				'scrypt-1.1.6/lib/crypto/crypto_scrypt-sse.c'
			],
		},
	],
}
